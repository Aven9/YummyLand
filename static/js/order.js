document.addEventListener('DOMContentLoaded', () => {
    let imgs = ['fastfood.jpeg','pasta.jpg','pizza.jpg','sushi.jpg'];
    let names = ['汉堡', '意大利面', '披萨', '寿司'];

    initializeOrder(4);
    function initializeOrder(number) {
        let template = Handlebars.compile(document.querySelector('#order').innerHTML);
        for (let i = 0; i < number; i++) {
            let imgPath = "../img/"+imgs[i%4];
            let name = names[i%4];
            let num = i;
            let price = Math.round(Math.random()*20);
            let tt_price = price*num;
            let item = {
                'img': imgPath,
                'name': name,
                'num': num,
                'price': price,
                'tt_price': tt_price

            };
            let order = template({'item': item});
            $('#current_order').append(order);
            $('#finished_order').append(order);
        }

    }
});