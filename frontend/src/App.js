
import './App.css';
import {useState, useEffect} from 'react';
import ArticleList from './components/ArticleList';

function App() {
  const [articles, setArticles] = useState([]);
  const [editedArticle, setEditedArticle] = useState([]);
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
  const editArticle = (article) => {
      console.log("Hello worlds")
      //setEditedArticle(article)
  }
  return (
    <div className="App">
      <h1>Flask and ReactJS Course</h1>
        <ArticleList  articles = {articles} editArticle = {editArticle}/>
    </div>
  );
}

export default App;
