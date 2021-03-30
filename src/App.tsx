import React,{useState,useEffect,Fragment,Suspense, lazy} from 'react'
import './App.css';
import InfoDB from './components/InfoDB';
import axios from 'axios';
const Lazy=lazy(()=>import('./components/Lazy'));
function App() {
  const [state,setState]=useState([]);
  const[image,setImage]=useState(null);
  const[action,setAction]=useState("")
  const[error,setError]=useState(0);
  let d=0;
  useEffect(()=>{
    axios.get("http://localhost:8000/api/uploaded/")
    .then((e:any)=>{
      setState(e.data)
      for(let i=0;i<e.data.length;i++){
        axios.get(`http://localhost:8000${e.data[i].image}`)
        .then((res:any)=>{
          setError(res.status)
        })
        .catch((err:any)=>{
         
        })
      }
    })
    .catch((err:any)=>{
      console.log(err)
    })
  },[])

  const handleSubmit=(e:any)=>{
    e.preventDefault();
    let formdata=new FormData();
    formdata.append('image',image,image.name);
    formdata.append('action',action);
    axios.post('http://localhost:8000/api/uploaded/',formdata,{
      headers:{
        'content-type':'multipart/form-data'
      }
    })
    .then((res:any)=>{
      getAgain();
      setError(200);
      console.log(res.data);
    })
    .catch((err:any)=>{
      console.log("error:");
    })
    var myvar=setInterval(mytimer,1000);
    function mytimer(){
      d++;
      if(d===6){
        clearInterval(myvar);
      }
      document.getElementById("noid").innerHTML=d.toLocaleString();
    }
  }
  const getAgain=()=>{
    axios.get("http://localhost:8000/api/uploaded/")
    .then((e:any)=>{
      setState(e.data)
    })
    .catch((err:any)=>{
      console.log(err)
    })
  }
  //https://cdn.myanimelist.net/images/characters/6/63870.jpg
  const handleChange=(e:any)=>{
    setImage(e.target.files[0]);
  }
  const handleContent=(e:any)=>{
    setAction(e.target.value);
  }
  const handleDelete=(e:any)=>{
    window.location.reload();
    axios.get(`http://localhost:8000/delete/${e}`)
    .then((res:any)=>{
      console.log(res)
    })
    .catch((err:any)=>{
      console.log(err)
    })
  }
  return (
       <Suspense fallback={
         <div style={{
           padding:" 2% 50% 50% 40%"
         }}>
           <img height="300px" width="300px"
           src="https://www.ancient-symbols.com/images/wp-image-library/fullsize/eye-of-god.jpg" alt="load.png"></img>
         </div>
       }>
         <div>
      <div id="div0">
      <form onSubmit={handleSubmit}>
       <input type="file" accept="image/png,image/jpeg" name="file" id="file" onChange={handleChange} required/>
       <p id="p0">THE EYE</p>
       <div id="div1">
       <select name="select" id="select" defaultValue={'NONE'} onChange={handleContent} required>
         <option value="NONE"  disabled hidden >Select</option>
         <option value="COLORIZED">colorized</option>
         <option value="GRAYSCALE">grayscale</option>
       </select>
       <button id="button0" type="submit"><span>Submit</span></button>
       </div>
      </form>
    </div>
    <p id="noid"></p>
     {state.map((e:any,i:any)=>{      
     return error===200?
     <ul key={e.id}>
       <li>
        <img id="image0" height="400px" width="400px" src={e.image} alt="images"></img>
        <div id="p1">
          <InfoDB index={i}></InfoDB>
        <button onClick={()=>handleDelete(e.id)}>Delete</button>
        </div>
       </li></ul>:<>
       <img height="400px" width="400px"
        src="https://www.edmundsgovtech.com/wp-content/uploads/2020/01/default-picture_0_0.png" alt="no-person.jpg"></img>
       </>
     })}
     <Lazy></Lazy>
     </div>
     </Suspense>
  )
}

export default App
