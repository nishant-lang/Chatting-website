//Get method for the chat message

// function get_chat_msg(){
//     const reciever = '{{chatting_with_user}}'
//     const sender='{{request.user.id}}'

// fetch(`http://127.0.0.1:8000/message/${reciever}`,{
//     method:'get',
//     headers: {'X-CSRFToken':'{{csrf_token}}',"Content-Type": "application/json"},
//     credentials:'same-origin',
//   })
//   .then(response=>{
//     return response.json()
//   })
//   .then((data)=>{
//     console.log(data)
//     //console.log(data.rec_msg[0].recive_chat)
//     //console.log(data.sen_msg[0].sender_chat)

// const renderHtml = function(data) {

//     for(let i=0;i<data.chating.length;i++){

//         //console.log(rec_msg[i].recive_chat)

//         if(data.chating[i].sender_id==sender){

//          const html = `<li class="clearfix admin_chat">
//                         <div class="chat-body clearfix  ">
//                          <p> ${data.chating[i].message} </p><br>
//                          </div>
//                          </li>`

//     document.querySelector('#msg_list').insertAdjacentHTML('beforeend',html)
//     document.querySelector('#msg_typing').value = ''
//     console.log("success")
//    }

//    else{
//     const html = `<li class="clearfix admin_chat ">
//         <div class="chat-body clearfix " style='float:left'  >
//          <p > ${data.chating[i].message} </p><br>

//             </div>
//             </li>`

//         document.querySelector('#msg_list').insertAdjacentHTML('beforeend',html)
//         document.querySelector('#msg_typing').value = ''
//         console.log("success")

//    }
// }

// }
// renderHtml(data)
// })

// }

//POST method for chat

//  function send_chat_msg(){
//     var msg=document.querySelector('#msg_typing').value
//     let data = {'msg':msg}
//     console.log('{{csrf_token}}')
//     console.log(msg)
//     const reciever = '{{chatting_with_user}}'

//     fetch(`http://127.0.0.1:8000/message/${reciever}`,{
//         method: "POST",
//         body:JSON.stringify(data),
//         headers: {'X-CSRFToken':'{{csrf_token}}',"Content-Type":"application/json"},
//         credentials:'same-origin',
//     })

//       .then(response => {
//         document.querySelector('#msg_list').innerHTML=''
//         get_chat_msg()

//     })
// }


