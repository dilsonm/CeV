#Crie um programa que abra um arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('coruja.mp3')
pygame.mixer.music.play()
pygame.event.wait()
