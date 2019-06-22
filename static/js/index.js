document.addEventListener('DOMContentLoaded', () => {
    let navs = ['快餐', '私房菜', '川菜', '粤菜', '北京菜', '西北菜', '西餐', '日料', '韩料', '烧烤'];
    for (let i in navs) {
        let navItem = addNavItem(navs[i]);
        navItem.onclick = ()=>{
            let category = navItem.innerHTML;
            window.location.href = Flask.url_for('shop_category', {'category': category});
        };
        document.getElementById('nav').append(navItem);
    }

    for (var i=0; i<4; i++){
        document.getElementById('discount').append(addStore());
    }

    for (var i=0; i<6; i++){
        document.getElementById('recommend').append(addStore());
    }

    function addNavItem(itemName) {
        let navItem = document.createElement('button');
        navItem.className = 'btn btn-success';
        navItem.type = 'button';
        // navItem.setAttribute('data-toggle', 'collapse');
        // navItem.setAttribute('data-target', 'collapseExample');
        // navItem.setAttribute('aria-expanded', 'false');
        // navItem.setAttribute('aria-controls', 'collapseExample');
        navItem.innerHTML = itemName;
        return navItem;
    }

    function addStore() {
        let row = document.createElement("div");
        row.className = "col-sm-4 col-lg-3 store";
        let card = document.createElement("div");
        card.className = 'card';
        let store = document.createElement('div');
        store.className = 'card-body';
        let storeImg = document.createElement("img");
        storeImg.className = "card-img-top";
        storeImg.src = "static/img/fastfood.jpeg";
        let storeName = document.createElement('h5');
        storeName.innerHTML = 'foo';
        let storeText = document.createElement('p');
        storeText.innerHTML = 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Optio deserunt fuga perferendis modi earum';
        let storeLink = document.createElement('a');
        storeLink.className = 'btn btn-success';
        storeLink.href = Flask.url_for('shop');
        storeLink.innerHTML = '去看看';
        store.append(storeImg);
        store.append(storeName);
        store.append(storeText);
        store.append(storeLink);
        card.append(store);
        row.appendChild(card);
        return row;
    }
});
