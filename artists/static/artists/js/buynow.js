function displayBuyNow(element) {
    console.log('Mouse over');
    var buyNowElement = element.querySelector(".buy-now");
    if (buyNowElement) {
        buyNowElement.style.display = "block";
    }
}

function hideBuyNow(element) {
    console.log('Mouse out');
    var buyNowElement = element.querySelector(".buy-now");
    if (buyNowElement) {
        buyNowElement.style.display = "none";
    }
}