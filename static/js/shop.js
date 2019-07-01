let cartKey = 'cart';
// localStorage.setItem(cartKey, JSON.stringify([]));
if (!localStorage.getItem(cartKey)) {
    localStorage.setItem(cartKey, JSON.stringify([]));
}

function manipulate(btn) {
    // console.log(btn);
    let op = btn.innerText;
    if (op === '+') {
        let label = btn.previousElementSibling;
        let num = parseFloat(label.innerText);
        let name = btn.parentElement.firstElementChild.innerHTML;
        num++;
        let cart_items = JSON.parse(localStorage.getItem(cartKey));
        for (let i in cart_items) {
            if (cart_items[i]['name'] === name) {
                cart_items[i]['num'] = num;
                localStorage.setItem(cartKey, JSON.stringify(cart_items));
                label.innerHTML = num+"";
                break;
            }
        }

    } else {
        let label = btn.nextElementSibling;
        let num = parseFloat(label.innerText);
        let name = btn.parentElement.firstElementChild.innerHTML;
        num--;
        let cart_items = JSON.parse(localStorage.getItem(cartKey));
        for (let i in cart_items) {
            if (cart_items[i]['name'] === name) {
                if (num>0) {
                    cart_items[i]['num'] = num;
                    label.innerHTML = num+"";
                    localStorage.setItem(cartKey, JSON.stringify(cart_items));
                    break
                } else {
                    cart_items.splice(i);
                    let card = document.getElementById(name);
                    card.parentNode.removeChild(card);
                    label.innerHTML = num+"";
                    localStorage.setItem(cartKey, JSON.stringify(cart_items));
                    break;
                }
            }
        }

    }

}

document.addEventListener('DOMContentLoaded', () => {

    loadHeadline();
    let types = ['热卖', '主食', '套餐', '小食'];
    let names = ['sushi', 'pizza', 'coffee', 'friedchips'];
    let imgs = ['fastfood.jpeg', 'pasta.jpg', 'pizza.jpg', 'sushi.jpg'];
    let nav_section = document.getElementById('navs');



    for (let i in types){
        let type = add_type(types[i]);
        document.getElementById('dishes').append(type);
        add_nav(types[i]);
        let layout = add_dish_layout();
        loadDishes(2, layout);
        document.getElementById('dishes').append(layout);
    }

    function loadHeadline() {
        let params = getParams();
        // console.log(params["sort"]);
        document.getElementById('headline').innerHTML = decodeURI(params["sort"]+"");
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
    }

    function loadDishes(dish_num, layout) {
        // 传入dishes数据进行解析...
        for (var j=0; j<dish_num; j++){
            let img = "../img/"+imgs[Math.round(Math.random()*3)];
            let price = Math.round(Math.random()*20);
            let name = names[j]+Math.round(Math.random()*20)+"."+Math.round(Math.random()*99);
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
       let button = draw_button('btn btn-success', '加购');
       button.type = 'button';
       button.dataset.toggle = "modal";
       button.dataset.target = "#exampleModalScrollable";
       button.onclick = () => {
           button.dataset.items = load_cart_items(img, price, name);
       }
       card_body.append(dish_img);
       card_body.append(dish_name);
       card_body.append(dish_price);
       card_body.append(button);
       card.append(card_body);
       component.append(card);
       return component;
   }

    $('#exampleModalScrollable').on('show.bs.modal', function (event) {
        let shopping_cart = document.getElementById("cart_body");
        while (shopping_cart.firstChild) {
            shopping_cart.removeChild(shopping_cart.firstChild);
        }
        let button = $(event.relatedTarget); // Button that triggered the modal
        let cart_items = button.data('items'); // Extract info from data-* attributes
        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.

        let template = Handlebars.compile(document.querySelector('#cart_card').innerHTML);
        for (let i in cart_items) {
            let card = template({"item": cart_items[i]});
            document.querySelector("#cart_body").innerHTML += card;
        }
    });


    // 提交订单
    document.getElementById('submit_cart').onclick = () => {
        //提交订单
        console.log(111);
    };
    

    function updateLocalStorage(name, num) {
            let cart_items = JSON.parse(localStorage.getItem(cartKey));
            for (let i in cart_items) {
                if (cart_items[i]['name'] === name) {
                    cart_items[i]['num'] = num;
                }
            }
            localStorage.setItem(cartKey, JSON.stringify(cart_items));
            return cart_items;
        }

    function load_cart_items(img, price, name) {
        let cart_items = JSON.parse(localStorage.getItem(cartKey));
        for (let i in cart_items) {
            if (cart_items[i]["name"] === name){
                cart_items[i]["num"]++;
                restore_cart(cart_items);
                return JSON.stringify(cart_items);
            }
        }
        let new_item = {"name": name, "price": price, "img": img, "num": 1}
        cart_items.push(new_item);
        restore_cart(cart_items);
        return JSON.stringify(cart_items);
    }

    function restore_cart(cart_items) {
        localStorage.setItem(cartKey, JSON.stringify(cart_items));
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