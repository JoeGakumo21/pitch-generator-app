
    // {/* // let like = document.querySelector('#like');
    // // let dislike =document.querySelector('#dislike');
    // // let input1 = document.querySelector('#input1');
    // // let input2 = document.querySelector('#input2');
    
  
    // // like.addEventListener('click',()=>{
    // //   input1.value = parseInt(input1.value) + 1;
    // //   input1.style.color = "#12ff00";
  
    // // })
  
    // // dislike.addEventListener('click',()=>{
    // //   input2.value = parseInt(input2.value) + 1;
    // //   input2.style.color = "#12ff00";
  
    // }) 
    var count=0;
   
    function upvote(){
        count++;
        document.getElementById('like').innerHTML=count;
    }
    var dislike=0;
    function downvote(){
        dislike++;
        document.getElementById('dislike').innerHTML=dislike;
    }
    var dislike1=0
    function downvote1(){
        dislike1++;
        document.getElementById('dislike1').innerHTML=dislike1;
    }
    var count1=0
    function upvote1(){
        count1++;
        document.getElementById('like1').innerHTML=count1;
    }