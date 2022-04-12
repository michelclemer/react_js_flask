
import './App.css';
import {useState, useEffect} from 'react';
import ArticleList from './components/ArticleList';

function App() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
     fetch('http://127.0.0.1:8090/api/get', {
        'method': 'GET',
        headers: {
            'Content-Type': 'applications/json'
        }
     })
     .then(resp => resp.json())
     .then(resp => setArticles(resp))
     .catch(error => console.log(error))
  }, [])

  return (
    <div className="App">
      <h1>Flask and ReactJS Course</h1>
        <ArticleList />
    </div>
  );
}

export default App;
