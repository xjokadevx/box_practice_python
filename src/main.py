from services import box

client = box.setConnBox()
print(client.user().get())

