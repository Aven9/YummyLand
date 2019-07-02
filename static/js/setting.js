const key = "4313174585d59c9cc9087fa77f30ff4b";
function requestURL(district) {
     return "https://restapi.amap.com/v3/config/district?key=" + key + "&keywords=" + district + "&subdistrict=1";
}

document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('add_address_btn').onclick = () => {

        console.log("click");
        let template = Handlebars.compile(document.querySelector('#address').innerHTML);
        let index = $('#default_address').parent().children().length;
        let address_part = template({'index': index});
        // console.log(address_part);
        $('#default_address').parent().append(address_part);
        // 修改选择器
        let selector1 = $('#address'+index).find('.province');
        let selector2 = $('#address'+index).find('.city');

        loadProvince(selector1);
        loadCities(selector2, '河南省');

        selector1[0].onchange = () => {
            // console.log('selector change');
            // console.log(selector1.val());
            let province = selector1.val();
            loadCities(selector2, province);
        };
    };

    function loadProvince(selector) {

        let url = requestURL('中国');
        // console.log(url);
        $.get(url, function (data, status) {
            if (status === 'success') {
                // console.log(data);
                let res = getSubdistricts(data);
                // console.log(res);
                layoutOptions(selector, res);
            }
        })
    }

    function loadCities(selector, province) {
        let url = requestURL(province);
        $.get(url, function (data, status) {
            if (status === 'success') {
                // console.log(data);
                let res = getSubdistricts(data);
                // console.log(res);
                while (selector[0].firstElementChild) {
                    selector[0].remove(selector[0].firstElementChild);
                }
                layoutOptions(selector, res);
            }
        })
    }

    function layoutOptions(selector, res) {
        for (let i = 0; i < res.length; ++i) {
            if (i === 0) {
                let html = '<option selected value="'+res[i]+'">'+res[i]+'</option>';
                selector.append(html);
            } else {
                let html = '<option value="'+res[i]+'">'+res[i]+'</option>';
                selector.append(html);
            }
        }
    }

    function getSubdistricts(data) {
        let districts = data['districts']['0']['districts'];
        let subdistricts = [];
        for (let i in districts){
            subdistricts.push(districts[i]["name"]);
        }
        return subdistricts;
    }

});

