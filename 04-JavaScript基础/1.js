const nameList = ['千古壹号', '许嵩', '解忧少帅'];

            function myTemplate() {
                // join('') 的意思是，把数组里的内容合并成一个字符串
                return `<ul>
                ${nameList
                    .map((item) => `<li>${item}</li>`)
                    .join('')}
                </ul>`;
            }
            document.body.innerHTML = myTemplate();