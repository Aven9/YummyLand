document.addEventListener('DOMContentLoaded', () => {
   var stores = ['四季度', '丹尼斯', '瞌睡🐱', '戴女士'];
   for (let i in stores){
       document.getElementById('shops').append(add_shop(stores[i]));
   }

   function add_shop(name) {
       let component = document.createElement('div');
       component.className = 'card';
       let card = document.createElement("div");
       card.className = 'card-body';
       let storeName = document.createElement('h4');
       storeName.innerHTML = name;

       // card.append(storeName);
       let store = document.createElement('div');
       store.className = 'row';

       store.append(add_shop_intro(name));

       for (var i=0; i<3; i++) {
           let dish = add_dish();
           store.append(dish);
       }
       card.append(store);
       component.append(card);
       return component;
   }

   function add_shop_intro(name) {
       let row = document.createElement("div");
        row.className = "col-sm-4 col-lg-3 dish";
        let card = document.createElement("div");
        card.className = 'card';
        let store = document.createElement('div');
        store.className = 'card-body';
        let storeImg = document.createElement('img');
        storeImg.src = '../static/img/shop_icon.png';
        let storeName = document.createElement('h5');
        storeName.innerHTML = name;
        let storeLink = document.createElement('a');
        storeLink.className = 'btn btn-outline-success container-fluid';
        storeLink.href = Flask.url_for('shop', {'shop_name': storeName.innerHTML});
        storeLink.innerHTML = '进入店铺';
        store.append(storeImg);
        store.append(storeName);
        store.append(storeLink);
        card.append(store);
        row.appendChild(card);
        return row;
   }

   function add_dish() {
        let row = document.createElement("div");
        row.className = "col-sm-4 col-lg-3 dish";
        let card = document.createElement("div");
        card.className = 'card';
        let store = document.createElement('div');
        store.className = 'card-body';
        let storeImg = document.createElement("img");
        storeImg.className = "card-img-top";

        let imgs = ['fastfood.jpeg', 'pasta.jpg', 'pizza.jpg', 'sushi.jpg'];
        let img = imgs[Math.round(Math.random()*3)];

        storeImg.src = '../static/img/'+img;
        let storeName = document.createElement('h5');
        storeName.innerHTML = 'foo';
        let storeText = document.createElement('p');
        storeText.innerHTML = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Optio deserunt fuga perferendis modi earum';
        let storeLink = document.createElement('a');
        storeLink.className = 'btn btn-success';
        storeLink.href = '#';
        storeLink.innerHTML = '去加购';
        store.append(storeImg);
        store.append(storeName);
        store.append(storeText);
        store.append(storeLink);
        card.append(store);
        row.appendChild(card);
        return row;
   }
});