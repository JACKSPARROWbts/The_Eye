import React,{useState,useEffect}from 'react'
import axios from 'axios'
var latlon=11.127122499999999+","+78.6568942;
function InfoDB(props:any) {
    const[state,setState]=useState([]);
    useEffect(()=>{
        axios.get("http://localhost:8000/infodb/api/leads/")
        .then((res:any)=>{
           setState(res.data);
           console.log(res.data)
        })
        .catch((err:any)=>{
            console.log(err);
        })
    },[])
    const renderifelse=(value:any)=>{
      if (state.length!==0){
      if(state[props.index].name==="millie"){
          return<ul key={props.index}>
              <p>NAME:  {state[props.index].name}</p>
              <p>CITY:  America</p>
              <p>GENDER: FEMALE</p>
              <p>CRIME: Being so Gorgeous</p>
              <p>CURRENT LOCATION:<a href={"https://www.google.com.sa/maps/search/"+ latlon}>hello</a></p>
          </ul> 
      }
      else if(state[props.index].name==="JaquinPhoenix"){
        return<ul key={props.index}>
         <p>NAME:  {state[props.index].name}</p>
         <p>CITY:  America</p>
              <p>GENDER: MALE</p>
              <p>CRIME: Killed people and ENEMY of Batman</p>
              <p>CURRENT LOCATION:<a href={"https://www.google.com.sa/maps/search/"+ latlon}>hello</a></p>
        </ul>
   }else if(state[props.index].name==="captain JACK"){
    return<ul key={props.index}>
    <p>NAME:  {state[props.index].name}</p>
    <p>CITY: City of GOLD</p>
         <p>GENDER: MALE</p>
         <p>CRIME:  Being a Pirate </p>
         <p>CURRENT LOCATION:<a href={"https://www.google.com.sa/maps/search/"+ latlon}>hello</a></p>
   </ul>
   }else if(state[props.index].name==="tony"){
    return<ul key={props.index}>
    <p>NAME:  {state[props.index].name}</p>
    <p>CITY: America</p>
         <p>GENDER: MALE</p>
         <p>CRIME: Destroyed city called Sokovia </p>
         <p>CURRENT LOCATION:<a href={"https://www.google.com.sa/maps/search/"+ latlon}>hello</a></p>
   </ul>
   }else if(state[props.index].name==="Eren Jaegar"){
    return<ul key={props.index}>
    <p>NAME:  {state[props.index].name}</p>
    <p>CITY: Shiganshina District</p>
         <p>GENDER: MALE</p>
         <p>CRIME:  Killed 1000 of Titans and Declared war on all country </p>
         <p>CURRENT LOCATION:<a href={"https://www.google.com.sa/maps/search/"+ latlon}>hello</a></p>
   </ul>
   }
      }
    }
    return (
        <div>
          {
         renderifelse(state)
          }
        </div>
    )
}

export default InfoDB

{/* <ul>{Imagenames[i]["pretty"].name}</ul> */}

{/* <div>
{state.map((data:any)=>{
   for(let i=0;i<value.length;i++){
       
       return(value[i].id===data.id)?
           <ul key={data.id}>
            <p>Name is {data.name}</p>
            <p>Location is {data.place}</p>
 <a href={"https://www.google.com.sa/maps/search/"+ latlon}>hello</a>
           </ul>
       :<ul>
           <p>Name is UNKNOWN</p>
           <p>Location is UNKNOWN</p>
       </ul>
   }
})}
</div> */}