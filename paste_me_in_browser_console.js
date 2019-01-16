data = {};

function fillcol(tr, col, value) {
  if (value !== undefined) {
    tr.children[col].children[0].value = score;
  }
}

var tbody = document
  .getElementById("frame_content")
  .contentWindow.document.getElementById("DataGrid1").children[0];
for (i in tbody.children) {
  if (i == 0) continue;
  var tr = tbody.children[i];
  if (tr.children === undefined) continue;
  var studentid = tr.children[1].innerText;
  var scores = data[parseInt(studentid)]; /* 假定导出表格学号栏数据格式为整数 */
  fillcol(tr, 2, scores.ps);
  fillcol(tr, 3, scores.qz);
  fillcol(tr, 4, scores.qm);
  fillcol(tr, 5, scores.zp);
}
