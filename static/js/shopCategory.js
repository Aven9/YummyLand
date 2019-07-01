document.addEventListener('DOMContentLoaded', () => {
    loadHeader();
    
   var stores = ['四季度', '丹尼斯', '瞌睡🐱', '戴女士'];

   loadStores(stores);

    function loadHeader() {
        let params = getParams();
        // console.log(params["sort"]);
        document.getElementById('shop_category_header').innerHTML = decodeURI(params["sort"]+"");
    }

    function getParams() {

        let str = window.location.search;
        let objURL = {};

        str.replace(
            new RegExp( "([^?=&]+)(=([^&]*))?", "g" ),
            function( $0, $1, $2, $3 ){
                objURL[ $1 ] = $3;
            }
        );
        return objURL;
    };

   function loadStores(stores) {
       for (let i in stores){
           document.getElementById('shops').append(add_shop(stores[i]));
       }
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
           let img = loadImg();
           let dish = add_dish(img);
           store.append(dish);
       }
       card.append(store);
       component.append(card);
       return component;
   }

   function loadImg() {
       let imgs = ['fastfood.jpeg', 'pasta.jpg', 'pizza.jpg', 'sushi.jpg'];
       let img = imgs[Math.round(Math.random()*3)];
       return img;
   }

   function add_shop_intro(name) {
       let row = document.createElement("div");
        row.className = "col-sm-4 col-lg-3 shop";
        let card = document.createElement("div");
        card.className = 'card';
        let store = document.createElement('div');
        store.className = 'card-body';
        let storeImg = document.createElement('img');
        storeImg.src = '../img/shop_icon.png';
        let storeName = document.createElement('h5');
        storeName.innerHTML = name;
        let storeLink = document.createElement('a');
        storeLink.className = 'btn btn-outline-success container-fluid';
        // storeLink.href = Flask.url_for('shop', {'shop_name': storeName.innerHTML});
        storeLink.href = "shop.html&shop_name="+storeName.innerText;
        storeLink.innerHTML = '进入店铺';
        store.append(storeImg);
        store.append(storeName);
        store.append(storeLink);
        card.append(store);
        row.appendChild(card);
        return row;
   }

   function add_dish(img) {
        let row = document.createElement("div");
        row.className = "col-sm-4 col-lg-3 dish";
        let card = document.createElement("div");
        card.className = 'card';
        let store = document.createElement('div');
        store.className = 'card-body';
        let storeImg = document.createElement("img");
        storeImg.className = "card-img-top";

        // need modify path...
        storeImg.src = '../img/'+img;
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