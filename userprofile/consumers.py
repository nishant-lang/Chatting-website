
# from email import message
import json
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth import get_user_model
# from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# from channels.consumer import AsyncConsumer
from userprofile.models import Chat_messages

User=get_user_model()

# class ChatConsumers(AsyncConsumer):
    
#     async def websocket_connect(self,event):
#         print('connected',event)
        
#         user=self.scope['user']
        
#         chat_room=f'user_chatroom_{user.id}'

#         self.chat_room=chat_room

#         await self.channel_layer.group_add(
#             chat_room,
#             self.channel_name
#         )

#         await self.send({
#             'type':'websocket.accept'
#         })

#     async def websocket_receive(self,event):
#         print('receive',event)
        
#         received_data=json.loads(event['text'])
#         msg=received_data.get('message')

#         sent_by_id=received_data.get('sent_by')
#         sent_to_id=received_data.get('sent_to')

    
#         # print(received_data)
#         # print(sent_by_id)
#         # print(sent_to_id)
    
#         if not msg:
#            print('Error::empty message')
#            return False

#         sent_by_user=await self.get_user_object(sent_by_id)
#         sent_to_user=await self.get_user_object(sent_to_id)

#         user_chat=await self.save_user_message(sent_by_id,sent_to_id,msg)

#         if not sent_by_user:
#             print('Error::Sent by user incorrect')
        
#         if not sent_to_user:
#             print('Error::Sent to user incorrect')

#         other_user_chat_room=f'user_chatroom_{sent_to_id}'

#         self_user=self.scope['user']

#         response={
#             'message':msg,
#             'sent_by':self_user.id,
           
#             }
        
#         await self.channel_layer.group_send(
#              other_user_chat_room,
#              {
#                 'type':'chat_message',
#                 'text':json.dumps(response)   
#             }
#         )

#         await self.channel_layer.group_send(
#              self.chat_room,
#              {
#                 'type':'chat_message',
#                 'text':json.dumps(response)   
#              }
#         )


#     async def websocket_disconnect(self,event):
#         print('disconnect',event)


#     async def chat_message(self,event):
#         print('chat_message',event)
        
#         await self.send({
#             'type':'websocket.send',
#             'text':event['text']
#         })


#     @database_sync_to_async
#     def get_user_object(self,user_id):
#         qs=User.objects.filter(id=user_id)
#         if qs.exists():
#             obj=qs.first()
#         else:
#             obj=None
#         return obj


#     @database_sync_to_async
#     def save_user_message(self,sender,receiver,user_message):
#         qs=Chat_messages.objects.create(receiver=receiver,sender=sender,user_chat=user_message)
#         if qs.exists():
#            user_obj=qs.first()
#         else:
#             user_obj=None
#         return user_obj


#     @database_sync_to_async
#     def get_user_object (self,user_id):
#         qs=User.objects.filter(id=user_id)
#         if qs.exists():
#             obj=qs.first()
#         else:
#             obj=None
#         return obj

   


class ChatConsumers(WebsocketConsumer):
    def connect(self):
        
        # self.receiver=self.scope["url_route"]["kwargs"]["reciever"]
        # sender=self.scope["url_route"]["kwargs"]["sender"]
        
        self.room_name = self.scope["sender"]

        self.room_group_name = "_" + self.room_name

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()
       

    def receive(self,text_data):
     
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        send_to = text_data_json['send_to']
        _from = text_data_json['from']
        
        save_user_message(_from,send_to,message)

        # print(send_to)
        channel_layer=get_channel_layer()

           
        async_to_sync(channel_layer.group_send)(
            f"_{send_to}",

            {
                'type': 'chat_message',
                'message':message, 
                'from':_from    
            }
        )

    def chat_message(self, event):

        message = event['message']
        to = event['from']

        self.send(text_data=json.dumps({
            'message': message,
            'from':to
        }))


    def disconnect(self):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

def save_user_message(sender,receiver,user_message):

    _sender=User.objects.filter(id=sender).first()
    _receiver=User.objects.filter(id=receiver).first()

    msg=Chat_messages.objects.model(receiver=_receiver,sender=_sender,user_chat=user_message) 
    msg.save()
    