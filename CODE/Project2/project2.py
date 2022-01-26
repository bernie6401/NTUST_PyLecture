import pygame
import random
import sys

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @staticmethod
    def distance(p1,p2):
        return ((p1.x - p2.x)** 2 + (p1.y - p2.y)** 2)**0.5
    def __str__(self):
        return f"{self.x},{self.y}"
    
class Deliver():
    def __init__(self,point,img):
        self.point = point
        self.img = img
        self.times = 60
        self.count = 0
        
    def setPath(self,path):
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.point.x,self.point.y)
        self.path =path
        self.current_position = 0 #設定當前點位
        
    def update(self):
        if self.times>self.count:
            if self.count == self.times-1:
                self.rect.x = world_coordinate[self.path[self.current_position]].x
                self.rect.y = world_coordinate[self.path[self.current_position]].y
            else:
                self.rect.x += (world_coordinate[self.path[self.current_position]].x - self.point.x)/self.times
                self.rect.y += (world_coordinate[self.path[self.current_position]].y - self.point.y)/self.times
            self.count+=1    
            screen.blit(self.img,  self.rect)
        else:
            if self.current_position<len(self.path)-1:
                self.point = world_coordinate[self.path[self.current_position]]
                self.count = 0
                self.current_position +=1
            else:
                screen.blit(self.img,  self.rect)
        
world_map = {0:"加拿大",1:"墨西哥",2:"巴西",3:"夏威夷",4:"俄羅斯",5:"中國",6:"澳大利亞",7:  "法國",8:"南非"}


graph =[[ 0 ,10,0 ,22,32,0 ,0 ,0 ,0 ], 
        [ 10,0 ,14,0 ,0 ,0 ,0 ,0 ,0 ],
        [ 0 ,14,0 ,0 ,0 ,0 ,20,0 ,0 ], 
        [ 22,0 ,0 ,0 ,0 ,15,20,0 ,0 ], 
        [ 32,0 ,0 ,0 ,0 ,8 ,0 ,20,0 ], 
        [ 0 ,0 ,0 ,15,8 ,0 ,0 ,0 ,24 ], 
        [ 0 ,0 ,20,20,0 ,0 ,0 ,0 ,12 ], 
        [ 0 ,0 ,0 ,0 ,20,0 ,0 ,0 ,18], 
        [ 0 ,0 ,0 ,0 ,0 ,24,12,18,0 ]]



graph_len = len(graph)

def minDistance(dist, sptSet):
  min_value = sys.maxsize
  min_index=0
  for v in range(graph_len): 
      if sptSet[v] == False and dist[v] <= min_value:
          min_value,min_index = dist[v],v
          
  return min_index

def dijkstra(graph, src) :
    dist=[sys.maxsize for i in range(graph_len)]      
    sptSet=[False for i in range(graph_len)]
    path = [-1 for i in range(graph_len)]
    dist[src] = 0
    for count in range(graph_len-1):
        u = minDistance(dist, sptSet)
        sptSet[u] = True
        for v in range(graph_len):
            if not sptSet[v] and graph[u][v] and dist[u] != sys.maxsize and dist[u] + graph[u][v] < dist[v]: 
                dist[v] = dist[u] + graph[u][v]
                path[v] = u
    return dist ,path

def getRealPath(path,src,dst):
    realPath = [dst]
    while dst != src:
        realPath.insert(0,path[dst])
        dst = path[dst]
    return realPath
    

def initPosition(delivers,buyers,delivers_img,buyers_img):
    shuffle_list = [1,2,3,4,5,6,7,8]
    random.shuffle(shuffle_list)
    for i in range(2):
        deliverPoint = Point(random.randint(0,1200),random.randint(0,650)) 
        delivers[i] = Deliver(deliverPoint,delivers_img[i])
        buyers[i] = shuffle_list[i]
        
    

world_coordinate = {0:Point(950, 150),1:Point(980, 320),2:Point(1190, 500),3:Point(790, 330)
                    ,4:Point(370, 120),5:Point(420, 270),6:Point(540, 560),7:Point(50, 180),8:Point(95, 580)}

pygame.init()
screen_width = 1300
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Project2')
delivers_img = [pygame.image.load('img/foodpanda.jpg'),pygame.image.load('img/ubereat.jpg')]
buyers_img = [pygame.image.load('img/buyerA.jpg'),pygame.image.load('img/buyerB.jpg')]
delivers=[None,None] #外送員座標
lucky_deliver = None
buyers = [None,None] #買家地點代號
delivery_path = [] #外送員送貨路徑
bg_img = pygame.image.load('img/bg.jpg')
screen.blit(bg_img, (0, 0))#背景圖

run = True
status = 0 #0:剛開啟程式 1:送貨員顯示
clock = pygame.time.Clock()

while run:
    clock.tick(60)
    screen.blit(bg_img, (0, 0))#背景圖
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: 
                if status ==0:
                    initPosition(delivers,buyers,delivers_img,buyers_img)
                    status+=1
                elif status ==1:
                    dist,path = dijkstra(graph,0)
                    if dist[buyers[0]]<dist[buyers[1]]:
                        delivery_path = getRealPath(path,0,buyers[0])[0:-1]
                        dist,path = dijkstra(graph,buyers[0])
                        delivery_path += getRealPath(path,buyers[0],buyers[1])
                        print('Foodpanda搶到訂單')
                    else:
                        delivery_path =getRealPath(path,0,buyers[1])[0:-1]
                        dist,path = dijkstra(graph,buyers[1])
                        delivery_path += getRealPath(path,buyers[1],buyers[0])
                        print('Ubereat搶到訂單！')
                    print('外送員路徑路徑：',end='')
                    for i in delivery_path:
                        print(world_map[i],end=' ')
                    lucky_deliver = delivers[0] if Point.distance(delivers[0].point, world_coordinate[0]) < Point.distance(delivers[1].point, world_coordinate[0]) else delivers[1]
                    lucky_deliver.setPath(delivery_path)
                    status+=1
    if status ==1:
        for i in range(2):
            screen.blit(delivers[i].img,(delivers[i].point.x,delivers[i].point.y))
            screen.blit(buyers_img[i],(world_coordinate[buyers[i]].x,world_coordinate[buyers[i]].y))
    if status ==2 :
        
        for i in range(2):
            screen.blit(buyers_img[i],(world_coordinate[buyers[i]].x,world_coordinate[buyers[i]].y))
        
        lucky_deliver.update()
                
    pygame.display.update()

pygame.quit()
