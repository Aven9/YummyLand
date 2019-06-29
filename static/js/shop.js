let cartKey = 'cart';
if (!localStorage.getItem(cartKey)) {
    localStorage.setItem(cartKey, JSON.stringify([]))
}
document.addEventListener('DOMContentLoaded', () => {
    let types = ['热卖', '主食', '套餐', '小食'];
    let imgs = ['fastfood.jpeg', 'pasta.jpg', 'pizza.jpg', 'sushi.jpg'];
    let nav_section = document.getElementById('navs');

    for (let i in types){
        let type = add_type(types[i]);
        document.getElementById('dishes').append(type);
        add_nav(types[i]);
        let layout = add_dish_layout();
        loadDishes(8, layout);
        document.getElementById('dishes').append(layout);
    }

    function loadDishes(dish_num, layout) {
        // 传入dishes数据进行解析...
        for (var j=0; j<dish_num; j++){
            let img = "../static/img/"+imgs[Math.round(Math.random()*3)];
            let price = Math.round(Math.random()*20);
            let name = '(*ﾟДﾟ*)';
            layout.append(add_dish(name, img, price));
        }
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
       let template = Handlebars.compile(document.querySelector("#cart_modal").innerHTML);
       let button = template({});
       card_body.append(dish_img);
       card_body.append(dish_name);
       card_body.append(dish_price);
       card_body.innerHTML+=button;
       // bind_add_cart();
       card.append(card_body);
       component.append(card);
       return component;
   }
    // function bind_add_cart() {
    //     document.querySelectorAll(".add_cart").forEach(button => {
    //         button.onclick = ()=>{
    //
    //         }
    //     })
    // }
    function load_cart(dish_img, dish_price, dish_name) {

        load_cart_items(cart, dish_img, dish_price, dish_name);
    }

    function load_cart_items(cart, dish_img, dish_price, dish_name) {


        cart_items = JSON.parse(localStorage.getItem(cartKey));
        for (let i in cart_items) {

        }
    }

    function load_cart_dish(item_layout, img_path, price, name) {
        // create elements.
        let dish_img = draw_img(img_path);
        let dish_price = document.createElement('label');
        dish_price.innerHTML = price;
        let dish_name = document.createElement('h5');
        dish_name.innerHTML = name;
        let input = document.createElement('input');
        input.type = "number";
        input.value = "1";
        let de_button = draw_button("btn btn-outline-success btn-round", "-");
        let in_button = draw_button("btn btn-outline-success btn-round", "+");
        de_button.onclick = () => {
            input.value = manipulate_value(input.value, "-");
        };
        in_button.onclick = () => {
            input.value = manipulate_value(input.value, "+");
        };

        // layout cart.
        let img_layout = draw_div("col-sm-2");
        img_layout.append(dish_img);
        let name_layout = draw_div("col-sm-4");
        name_layout.append(dish_name);
        let de_layout = draw_div("col-sm-1");
        de_layout.append(de_button);
        let input_layout = draw_div("col-sm-1");
        input_layout.append(input);
        let in_layout = draw_div("col-sm-1");
        in_layout.append(in_button);
        let price_layout = draw_div("col-sm-2");
        price_layout.append(price);

        item_layout.append(img_layout);
        item_layout.append(name_layout);
        item_layout.append(de_layout);
        item_layout.append(input_layout);
        item_layout.append(in_layout);
        item_layout.append(price_layout);
    }

    function manipulate_value(value, operation) {
        if (operation === '+') {
            value++;
        } else if (operation === '-' && value > 0) {
            value--;
        }
        return value;
    }

    function draw_button(className, innerText) {
        let button = document.createElement("button");
        button.className = className;
        button.innerHTML = innerText;
        return button;
    }

    function draw_img(img_path) {
        let img = document.createElement('img');
        img.src = img_path;
        return img;
    }

    function draw_div(className) {
        let div = document.createElement("div");
        div.className = className;
        return div;
    }
});