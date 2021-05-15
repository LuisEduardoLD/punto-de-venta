window.addEventListener('load', (e) => {
   var btnsubmit = document.getElementById('btnsubmit')
   var form = document.getElementById('form')

   btnsubmit.addEventListener('click', () => {
      form.submit();
   });

});
