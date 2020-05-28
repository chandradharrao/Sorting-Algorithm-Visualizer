import random
import PySimpleGUI as sg
import pygame
import numpy as np

sg.theme('DarkAmber')
layout1 = [[sg.Text("Sorting visualizer")],
          [sg.Button("Start")],[sg.Button("Exit")]]

screen1 = sg.Window("Sorting Visualizer",layout1)
choice1 = True
while choice1:
    entry1,values1 = screen1.read()
    if entry1 is None:
        break
    if entry1 == "Start":
        choice1 = False
        screen1.close()
        choice2 = True
        layout2 = [[sg.Text("Sorting visualizer")],
              [sg.Button("Selection Sort")],[sg.Button("Counting Sort")],
                [sg.Button("Exit")]]
        screen2 = sg.Window("Sorting Visualizer",layout2)
        while choice2:
            entry2,values2 = screen2.read()
            if entry2 == "Selection Sort":
                screen2.close()
                pygame.init()
                window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                pygame.display.set_caption("Sorting Visualizer")
                
                class bars():
                    def __init__(self,x,y,height,width):
                        self.height = height
                        self.x = x  #initial x co ordinate to maintain distance from x axis
                        self.y = y  #initial y co ordinate to maintain distance from y axis
                        self.width = width
                    def selectionSort(self):
                        for i in range(len(self.height)):
                            min_indx = i
                            for j in range(i+1,len(self.height)):
                                if self.height[j] < self.height[min_indx]:
                                    min_indx = j
                            self.height[i],self.height[min_indx] = self.height[min_indx],self.height[i]
                            window.fill((0,0,0))
                            show()
                            pygame.display.update()
                            pygame.time.delay(30)
                            debugPrint(self.height,False)
                        debugPrint(self.height,False)
                    def countingSort(self):
                        n = len(self.height)
                        k = max(self.height)
                        count_arr = [0]*(k+1)
                        for i in range(0,k+1):
                            count_arr[i] = self.height.count(i)
                        for i in range(1,k+1):
                            count_arr[i] = count_arr[i-1]+count_arr[i]
                        for i in self.height:
                            ind = count_arr[i] - 1
                            self.res[ind] = i
                            count_arr[i] = count_arr[i] - 1
                            window.fill((0,0,0))
                            show_exe2()
                            pygame.display.update()
                            pygame.time.delay(30)
                            debugPrint(self.res,False)
                        debugPrint(self.res,False)
                def debugPrint(content,state):
                    if state == True:
                        print("{}".format(content))
                def show():
                    for i in range(len(algo.height)):
                        pygame.draw.rect(window,(255,0,0),((algo.x)+10*i,algo.y,algo.width,algo.height[i]))
                def show_exe2():
                    for i in range(len(algo.res)):
                        pygame.draw.rect(window,(255,0,0),((algo.x)+10*i,algo.y,algo.width,algo.res[i]))

                randnums = [0]*180
                for i in range(180):
                    #no of ele is 180
                    x = random.randint(0, 800)
                    #size is 800
                    randnums[i] = x
                algo = bars(40,40,randnums,5)
                running = True
                while running:
                    exe = False
                    keys = pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if keys[pygame.K_SPACE]:
                            exe = True
                            pygame.time.delay(20)
                        if keys[pygame.K_q]:
                            running = False
                        if exe == False:
                            window.fill((0,0,0))
                            show()
                            pygame.display.update()
                        else:
                            algo.selectionSort()
                pygame.quit()
            elif entry2 == "Counting Sort":
                screen2.close()
                pygame.init()
                window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                pygame.display.set_caption("Sorting Visualizer")




                class bars():
                    def __init__(self, x, y, height, width, res):
                        self.height = height
                        self.x = x  # initial x co ordinate to maintain distance from x axis
                        self.y = y  # initial y co ordinate to maintain distance from y axis
                        self.width = width
                        self.res = res


                    def countingSort(self):
                        n = len(self.height)
                        k = max(self.height)
                        count_arr = [0] * (k + 1)
                        for i in range(0, k + 1):
                            count_arr[i] = self.height.count(i)
                        for i in range(1, k + 1):
                            count_arr[i] = count_arr[i - 1] + count_arr[i]
                        for i in self.height:
                            ind = count_arr[i] - 1
                            self.res[ind] = i
                            count_arr[i] = count_arr[i] - 1
                            window.fill((0, 0, 0))
                            show_exe2()
                            pygame.display.update()
                            pygame.time.delay(30)
                            debugPrint(self.res, False)
                        debugPrint(self.res, False)


                def debugPrint(content, state):
                    if state == True:
                        print("{}".format(content))


                def show():
                    for i in range(len(algo.height)):
                        pygame.draw.rect(window, (255, 0, 0), ((algo.x) + 10 * i, algo.y, algo.width, algo.height[i]))


                def show_exe2():
                    for i in range(len(algo.res)):
                        pygame.draw.rect(window, (255, 0, 0), ((algo.x) + 10 * i, algo.y, algo.width, algo.res[i]))


              
                
                randnums = [0] * 180
                for i in range(180):
                    # no of ele is 180
                    x = random.randint(0, 800)
                    # size is 800
                    randnums[i] = x
                algo = bars(40, 40, randnums, 5, [0] * 180)
                running = True
                while running:
                    exe = False
                    keys = pygame.key.get_pressed()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if keys[pygame.K_SPACE]:
                            exe = True
                            pygame.time.delay(20)
                        if keys[pygame.K_q]:
                            running = False
                        if exe == False:
                            window.fill((0, 0, 0))
                            show()
                            pygame.display.update()
                        else:
                            algo.countingSort()
                pygame.quit()
            elif entry2 == "Exit":
                screen2.close()
    elif entry1 == "Exit":
        screen1.close()
