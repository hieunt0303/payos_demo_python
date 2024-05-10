
document.getElementById('submit').addEventListener('click',submitForm)
async function submitForm(){
  const response = await fetch('/create-payment-link',{
    method:'post'
  })
  const payment = await response.json()
  console.log(payment)
  window.open(payment.checkoutUrl);


}