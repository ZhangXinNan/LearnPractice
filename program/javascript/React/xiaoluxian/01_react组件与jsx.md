
[【2025年版】react快速入门](https://www.bilibili.com/video/BV1ZH3yzKEdj/?spm_id_from=333.337.search-card.all.click&vd_source=29d95893817d1309f105b96460fb11e9)


# 1 React组件与JSX

## 1.1 React组件的特点
使用jsx开发，最纯粹的js开发。

React组件可以是一个方法（函数组件），也可以是一个class（Class组件）。
可以直接在js文件里写一段html来作为一个组件，也可以写成一个单独的jsx或者js文件。

看一下App.js里的代码：
```js
import logo from './logo.svg';
import './App.css';

// 这个App()方法是一个组件
function App() {
  return (
    //jsx可以直接写html，而普通js不可以。
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

```


函数组件：
```js
function hello(){
    return (
        <div>
            <p>Hello</p>
        </div>

    )
}
```

Class组件：
```js
class Hello extends React.Component {
    render() {
        return (
            <div>
                <p>Hello</p>
            </div>
        )
    }
}
```

## 1.2 JSX的特点
- 可以直接写在js文件中
  - React利用babel做了对js的编译，所以我们直接在js里写jsx。
- 写法接近js
  - jsx和js写法一样，不同点在于可以更方便的写html在js里。

