(this["webpackJsonpmytweeter-web"]=this["webpackJsonpmytweeter-web"]||[]).push([[0],{12:function(e,t,c){},13:function(e,t,c){},15:function(e,t,c){"use strict";c.r(t);var n=c(1),s=c.n(n),a=c(6),r=c.n(a),i=(c(12),c.p+"static/media/logo.6ce24c58.svg"),o=(c(13),c(7)),l=c(2);var j=c(0);function b(e){var t=s.a.createRef(),c=Object(n.useState)([]),a=Object(l.a)(c,2),r=a[0],i=a[1];return Object(j.jsxs)("div",{className:e.className,children:[Object(j.jsx)("div",{className:"col-12 mb-3",children:Object(j.jsxs)("form",{onSubmit:function(e){e.preventDefault();var c=t.current.value,n=Object(o.a)(r);n.unshift({content:c,likes:0,id:12313}),i(n),t.current.value=""},children:[Object(j.jsx)("textarea",{ref:t,required:!0,className:"form-control",name:"tweet"}),Object(j.jsx)("button",{type:"submit",className:"btn btn-primary my-3",children:"Tweet"})]})}),Object(j.jsx)(u,{newTweets:r})]})}function u(e){var t=Object(n.useState)([]),c=Object(l.a)(t,2),s=c[0],a=c[1],r=Object(n.useState)([]),i=Object(l.a)(r,2),b=i[0],u=i[1];return Object(n.useEffect)((function(){var t=Object(o.a)(e.newTweets).concat(s);t.length!==b.length&&u(t)}),[e.newTweets,b,s]),Object(n.useEffect)((function(){!function(e){var t=new XMLHttpRequest;t.responseType="json",t.open("GET","http://localhost:8000/api/tweets/"),t.onload=function(){e(t.response,t.status)},t.onerror=function(t){console.log(t),e({message:"The request was an error"},400)},t.send()}((function(e,t){200===t?a(e):alert("There was an error")}))}),[s]),b.map((function(e,t){return Object(j.jsx)(p,{tweet:e,className:"my-5 py-5 border bg-white text-dark"},"".concat(t,"-{item.id}"))}))}function d(e){var t=e.tweet,c=e.action,s=Object(n.useState)(t.likes?t.likes:0),a=Object(l.a)(s,2),r=a[0],i=a[1],o=Object(n.useState)(!0===t.userLike),b=Object(l.a)(o,2),u=b[0],d=b[1],p=e.className?e.className:"btn btn-primary btn-sm",m=c.display?c.display:"Action",O="like"===c.type?"".concat(r," ").concat(m):m;return Object(j.jsx)("button",{className:p,onClick:function(e){e.preventDefault(),"like"===c.type&&(!0===u?(i(r-1),d(!1)):(i(r+1),d(!0)))},children:O})}function p(e){var t=e.tweet,c=e.className?e.className:"col-10 mx-auto col-md-6";return Object(j.jsxs)("div",{className:c,children:[Object(j.jsxs)("p",{children:[t.id," - ",t.content]}),Object(j.jsxs)("div",{className:"btn btn-group",children:[Object(j.jsx)(d,{tweet:t,action:{type:"like",display:"Likes"}}),Object(j.jsx)(d,{tweet:t,action:{type:"unlike",display:"Unlike"}}),Object(j.jsx)(d,{tweet:t,action:{type:"retweet",display:""}})]})]})}var m=function(){return Object(j.jsx)("div",{className:"App",children:Object(j.jsxs)("header",{className:"App-header",children:[Object(j.jsx)("img",{src:i,className:"App-logo",alt:"logo"}),Object(j.jsxs)("p",{children:["Edit ",Object(j.jsx)("code",{children:"src/App.js"})," and save to reload."]}),Object(j.jsx)("div",{children:Object(j.jsx)(b,{})}),Object(j.jsx)("a",{className:"App-link",href:"https://reactjs.org",target:"_blank",rel:"noopener noreferrer",children:"Learn React"})]})})},O=function(e){e&&e instanceof Function&&c.e(3).then(c.bind(null,16)).then((function(t){var c=t.getCLS,n=t.getFID,s=t.getFCP,a=t.getLCP,r=t.getTTFB;c(e),n(e),s(e),a(e),r(e)}))},f=document.getElementById("root");f&&r.a.render(Object(j.jsx)(s.a.StrictMode,{children:Object(j.jsx)(m,{})}),f);var h=document.getElementById("mytweeter");h&&r.a.render(Object(j.jsx)(s.a.StrictMode,{children:Object(j.jsx)(b,{})}),h),O()}},[[15,1,2]]]);
//# sourceMappingURL=main.6ed587b4.chunk.js.map