#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Importamos las bibliotecas necesarias para las bibliotecas de python

import telebot  
from telebot import types
TOKEN="246437680:AAGdvmfrO8kWmxCEOhFIi22khRgFxWkxF9I"  
bot = telebot.TeleBot(TOKEN)

#Esto es lo que hace cuando el usuario le da al \/start

@bot.message_handler(commands=['start'])
def send_welcome(message):  
    cid = message.chat.id
    bot.send_message( cid, "Bienvenido a DeliveryTest BOT - Aquí están las opciones para empezar a elegir\n")
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup = types.ReplyKeyboardMarkup()
    itembtna = types.KeyboardButton('Oferta del día')
    itembtnv = types.KeyboardButton('Combos')
    itembtnc = types.KeyboardButton('Seleccion manual')
    itembtnd = types.KeyboardButton('Ayuda')
    itembtne = types.KeyboardButton('Acerca de')
    markup.row(itembtna, itembtnv)
    markup.row(itembtnc, itembtnd, itembtne)
    bot.send_message(cid, "Choose one letter:", reply_markup=markup)

#Acá es hacer funciones para cada menu

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    cid = message.chat.id 
    
    if message.text=="Oferta del día":
        cid = message.chat.id  
        # sendPhoto
        photo = open('img/oferta.jpeg', 'rb')
        bot.send_photo(cid, photo)
        bot.send_message( cid, "[b]Oferta del día[/b]\n\nAlguna oferta deliciosa en la cual puede sonar a beneficiosa para el antojo de uno, no?\n\nPrecio: 120")
    elif message.text=="Acerca de":
        cid = message.chat.id  
        # sendPhoto
        bot.send_message( cid, "[b]Oferta del día[/b]\n\nAlguna oferta deliciosa en la cual puede sonar a beneficiosa para el antojo de uno, no?\n\nPrecio: 120")
    else:
        cid = message.chat.id 
        bot.send_message(cid, "Trabajo en proceso")
    

##############     
bot.polling(none_stop=True)  
while True: #Infinite loop  
    pass