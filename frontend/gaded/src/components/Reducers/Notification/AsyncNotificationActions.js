 import * as actions from './NotificationAction'; 
import Axios from '../../Axios/Axios';








export const asyncFetchNotification =(page,from)=>{


    let url='/getUserNotification/'
    if(page){
        url=page
    }

   return dispatch=>{
        Axios({
            method:'get',
            url:url,
            headers:{
                Authorization:'Token '.concat('d15329184e916c5fa6b464c91742bf7b1ab791e9'),
            },
        })
        .then(res=>{
            if(from==='update'){
                dispatch(actions.fetchNotificationsUpdate(res.data))

            }else if(){
                
            
        }else{
                dispatch(actions.fetchNotifications(res.data))

            }
        })
        .catch(er=>{
        })
       
        
    }
}




// export const asyncNotificationCount=()=>{

//     return  dispatch=>{
//         Axios({
//             method:'get',
//             url:'/getNotificationCount/',
//             headers:{
//                 Authorization:'Token '.concat('d15329184e916c5fa6b464c91742bf7b1ab791e9'),
//             },
//         })
//         .then(res=>{
//             dispatch(actions.getNotificationCount(res.data.notificationCount))})
// }}