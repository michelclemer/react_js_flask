
import React from 'react';

function ArticleList(props){
    return (
        <div>
            {props.articles && articles.map( article =>{
        return (
            <div key= {article.id}>
                <h2>{article.title}</h2>
                <p>{article.body}</p>
                 <p>{article.date}</p>

                </div>
        )
      }

      )};
        </div>
    )
}