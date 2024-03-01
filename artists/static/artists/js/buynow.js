function displayBuyNow(element) {
    var buyNowElements = element.getElementsByClassName("buy-now");
    if (buyNowElements.length > 0) {
        buyNowElements[0].style.display = "block";
    }
}

function hideBuyNow(element) {
    var buyNowElements = element.getElementsByClassName("buy-now");
    if (buyNowElements.length > 0) {
        buyNowElements[0].style.display = "none";
    }
}