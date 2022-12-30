from django.shortcuts import render

# Create your views here.
# 刪除留言
class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')      