/*
 * 使用方法：
 * 1. 将 data = {} 中的 `{}` 替换为 extract.py 生成的文件内容
 * 2. 打开浏览器控制台（通常按 F12 快捷键）
 * 3. 将该文件复制粘贴至脚本最下方输入栏，回车。
*/

data = {};

var tbody = document
  .getElementById("frame_content")
  .contentWindow.document.getElementById("DataGrid1").children[0];
for (i in tbody.children) {
  if (i == 0) continue;
  var tr = tbody.children[i];
  if (tr.children === undefined) continue;
  var studentid = tr.children[1].innerText;
  var score = data[parseInt(studentid)]; /* 假定导出表格学号栏数据格式为整数 */
  if (score === undefined) continue; /* 学号不匹配，不填充 */
  tr.children[5].children[0].value = score; /* 将成绩填充表格第 5 栏（期末成绩） */
}
