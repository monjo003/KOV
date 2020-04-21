import React, {useState, useEffect} from 'react'; 
import './App.css';

function App(){

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    const data = await fetch('https://coronavirus-19-api.herokuapp.com/countries/ethiopia');
  
    const item = await data.json();
    console.log(item);
}

  return (
    <div>
<h1>abce</h1>
    </div>
  );

}
export default App;