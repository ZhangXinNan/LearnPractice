
# 1 安装
## 1.1 安装node.js

## 1.2 npm 安装 vue
```bash
npm install vue
```
## 1.3 安装vue-cli
```bash
npm install --global @vue/cli
```

# 2 使用vite构建

```bash
# 1 创建命令
npm create vite@latest

# 2 具体配置

# npm 7+, extra double-dash is needed:
npm create vite@latest my-vue-app -- --template vue
```

# 3 使用vue-cli构建
```bash
mkdir study_vuecli

cd study_vuecli

vue create oneweb

cd oneweb
npm run serve

```

目录结构

- src           前端业务代码
  - assets          资源存放目录，存放共用的css/图片/js等静态资源文件，这里的资源会被webpack构建。
  - components      组件目录，存放前端业务代码文件，一个页面由多个组件组成，一个前端项目由不同的页面组成。目标创建时自动产生HelloWorld.vue组件。
  - App.vue         前端组件文件，是Vue文件入口界面。设计标准为三段式：`模板<template>/应用程序脚本<script>/样式<style>`
  - main.js         对应App.vue文件创建Vue实例App。是入口js文件。
- node_modules  创建项目时，在线加载的项目依赖包
- public        用来存放index.html及项目中用到的一些静态资源文件
- package.json  npm包配置文件




