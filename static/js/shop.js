document.addEventListener('DOMContentLoaded', () => {
    let types = ['xxx', 'yyy', 'zzz', 'ooo'];
    let imgs = ['fastfood.jpeg', 'pasta.jpg', 'pizza.jpg', 'sushi.jpg'];
    let nav_section = document.getElementById('navs');

    for (let i in types){
        let type = add_type(types[i]);
        document.getElementById('dishes').append(type);
        add_nav(types[i]);
        let layout = add_dish_layout();
        for (var j=0; j<6; j++){
            let img = "../static/img/"+imgs[Math.round(Math.random()*3)];
            let price = Math.random()*20;
            let name = '(*ﾟДﾟ*)';
            layout.append(add_dish(name, img, price));
        }
        document.getElementById('dishes').append(layout);
    }

    function add_nav(name) {
        let p = document.createElement('p');
        let a = document.createElement('a');
        // a.className = 'nav-link';
        a.innerHTML = name;
        a.href = '#'+name;
        p.append(a);
        nav_section.append(p);
    }


   function add_type(type_name) {
        let hr = document.createElement('hr');
        document.getElementById('dishes').append(hr);
       let type = document.createElement('p');
       type.className = 'dish_type';
       type.id = type_name;
       type.innerHTML = type_name;
       return type;
   }
   function add_dish_layout() {
       let row = document.createElement('div');
       row.className = 'row';
       return row;
   }
   function add_dish(name, img, price) {
       let component = document.createElement("div");
       component.className = 'col-sm-6 col-lg-4 dish';
       let card = document.createElement('div');
       card.className = 'card';
       let card_body = document.createElement('div');
       card_body.className = 'card-body';
       let dish_name = document.createElement('h5');
       dish_name.className = 'dish_name';
       dish_name.innerHTML = name;
       let dish_img = document.createElement('img');
       dish_img.className = 'card-img-top';
       dish_img.src = img;
       let dish_price = document.createElement('p');
       dish_price.className = 'dish_price';
       dish_price.innerHTML = price;
       let button = document.createElement('button');
       button.className = 'btn btn-success add_cart';
       button.innerHTML = '加购';
       button.onclick = ()=>{
           // 弹出加购数量框；
       };
       card_body.append(dish_img);
       card_body.append(dish_name);
       card_body.append(dish_price);
       card_body.append(button);
       card.append(card_body);
       component.append(card);
       return component;
   }
});