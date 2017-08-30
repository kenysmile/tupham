import os
from mongoengine import *
from flask import *
import mlab
mlab.connect()

app = Flask(__name__)

app.config["IMG_PATH"] = os.path.join(app.root_path, "images")

class Foody(Document):
    title = StringField()
    name = StringField()
    image = StringField()
    address = StringField()
    location1 = StringField()
    rating = FloatField()

sunsetsoda = Foody("sunsetsoda", "Sunset soda", "http://sohanews.sohacdn.com/zoom/700_438/2016/photo-1-1463642543176-0-33-123-200-crop-1463642656027.jpg",
                    "245/4 Nguyễn Trãi, Quận 1, Hồ Chí Minh", "https://www.google.com/maps/place/245%2F4+Nguy%E1%BB%85n+Tr%C3%A3i,+Nguy%E1%BB%85n+C%C6%B0+Trinh,+Qu%E1%BA%ADn+1,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.764489,106.6856232,17z/data=!3m1!4b1!4m5!3m4!1s0x31752f19d9a1c407:0xa15ba58fdc46f25d!8m2!3d10.764489!4d106.687811", 9.5)
sodatao = Foody("sodatao", "Soda Táo", "http://cdn.dayphache.edu.vn/images/congthucphache/hinh-anh-soda-tao-xanh.jpg", "331 Trần Bình Trọng, 4, Quận 5, Hồ Chí Minh", "https://www.google.com/maps/place/331+Tr%E1%BA%A7n+B%C3%ACnh+Tr%E1%BB%8Dng,+ph%C6%B0%E1%BB%9Dng+4,+Qu%E1%BA%ADn+5,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.763149,106.6766786,17z/data=!3m1!4b1!4m8!1m2!2m1!1zMzMxIFRy4bqnbiBCw6xuaCBUcuG7jW5nLCA0LCBRdeG6rW4gNSwgSOG7kyBDaMOtIE1pbmg!3m4!1s0x31752f1dd602e723:0xb841a8dd2a6bc1e4!8m2!3d10.7631437!4d106.6788673", 8.0)
trasuaphomaituoi = Foody("trasuaphomaituoi", "Trà sữa phô mai tươi", "http://cdn01.diadiemanuong.com/ddau/640x/teens-sai-gon-dieu-dung-9-quan-tra-sua-pho-mai-chi-tu-15k-cuc-kich-thich-580a0e6e636123107523839208.jpg", "113 Phan Xích Long, phường 1, Quận Phú Nhuận, Hồ Chí Minh", "https://www.google.com/maps/place/113+Phan+X%C3%ADch+Long,+ph%C6%B0%E1%BB%9Dng+1,+Ph%C3%BA+Nhu%E1%BA%ADn,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.7990867,106.6842004,17z/data=!3m1!4b1!4m5!3m4!1s0x317528d046d7cd0d:0x3f3fc9431e041412!8m2!3d10.7990814!4d106.6863891", 7.0)
pizzahaisan = Foody("pizzahaisan", "Pizza hải sản", "http://anh.24h.com.vn/upload/4-2014/images/2014-12-25/1419475520-cuoi-nam-ru-nhau-di-an-pizza-2.jpg", "151/2B Nguyễn Ảnh Thủ, Huyện Hóc Môn, Hồ Chí Minh", "https://www.google.com/maps/place/151%2F2B+Nguy%E1%BB%85n+%E1%BA%A2nh+Th%E1%BB%A7,+Trung+Ch%C3%A1nh,+T%C3%A2n+Xu%C3%A2n,+H%C3%B3c+M%C3%B4n,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.8579483,106.6065413,17z/data=!3m1!4b1!4m5!3m4!1s0x31752a3e4b99ff9b:0x1c2fb1e5953ff668!8m2!3d10.857943!4d106.60873", 8.0)
fruitteablueberry = Foody("fruitteablueberry", "Fruit Tea Blueberry", "https://s-media-cache-ak0.pinimg.com/originals/9a/0a/86/9a0a866d23f5f51d3001cec2128ee13f.jpg", "47/5F đường Song Hành, Huyện Hóc Môn, Hồ Chí Minh", "https://www.google.com/maps/place/47%2F5D+%C4%90%C6%B0%E1%BB%9Dng+Song+H%C3%A0nh+QL+22,+Trung+Ch%C3%A1nh,+T%C3%A2n+Xu%C3%A2n,+H%C3%B3c+M%C3%B4n,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.8603054,106.6041619,17z/data=!3m1!4b1!4m5!3m4!1s0x31752a1550bf79a1:0xc5ff85924db5ad7a!8m2!3d10.8603001!4d106.6063506", 8.5)
hongtrasuibot = Foody("hongtrasuibot", "Hồng trà sủi bọt", "http://static.diadiemanuong.com/review/52040/kkk.jpg", "485 Sư Vạn Hạnh, phường 9, Quận 10, Hồ Chí Minh", "https://www.google.com/maps/place/485+S%C6%B0+V%E1%BA%A1n+H%E1%BA%A1nh,+ph%C6%B0%E1%BB%9Dng+9,+Qu%E1%BA%ADn+10,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.7688842,106.6687002,17z/data=!3m1!4b1!4m5!3m4!1s0x31752ede1cbfe961:0x55bfe8ab97303d83!8m2!3d10.7688789!4d106.6708889", 7.5)
trasua = Foody("trasua", "Trà sữa", "https://s-media-cache-ak0.pinimg.com/originals/f2/d1/96/f2d196363da420e1212d74e2553a71f3.jpg", "98-126 Nguyễn Tri Phương, Phường 7, Quận 5, Hồ Chí Minh", "https://www.google.com/maps/place/98-%3E126+Nguy%E1%BB%85n+Tri+Ph%C6%B0%C6%A1ng,+Ph%C6%B0%E1%BB%9Dng+7,+Qu%E1%BA%ADn+5,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.7540384,106.6675623,17z/data=!3m1!4b1!4m5!3m4!1s0x31752efbf2b7d7b9:0x4474da772512a3f1!8m2!3d10.7540331!4d106.669751", 7.5)
laukem = Foody("laukem", "Lẩu kem", "https://tea-1.lozi.vn/v1/images/resized/lau-kem-7882-1409395611?w=480&type=s", "6A Trần Hưng Đạo, Phạm Ngũ Lão, Quận 1, Hồ Chí Minh", "https://www.google.com/maps/place/6A+Tr%E1%BA%A7n+H%C6%B0ng+%C4%90%E1%BA%A1o,+Ph%E1%BA%A1m+Ng%C5%A9+L%C3%A3o,+Qu%E1%BA%ADn+1,+H%E1%BB%93+Ch%C3%AD+Minh,+Vi%E1%BB%87t+Nam/@10.7693412,106.6940223,17z/data=!3m1!4b1!4m5!3m4!1s0x31752f3e4f599229:0xfa8397214daa9999!8m2!3d10.7693359!4d106.696211", 8)
#
# sunsetsoda.save()
# sodatao.save()
# trasuaphomaituoi.save()
# pizzahaisan.save()
# fruitteablueberry.save()
# hongtrasuibot.save()
# trasua.save()
# laukem.save()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/product')
def product():
    # return render_template("product.html", foodys=Foody.objects())
    return render_template("product.html", foodys=Foody.objects())
    # return render_template("product.html", foody = Foody.objects().with_index[product_index])

@app.route('/productdetail/<int:product_item>')
def productdetail(product_item):
    return render_template("productdetail.html", foody=Foody.objects()[product_item])


if __name__ == '__main__':
    app.run()
