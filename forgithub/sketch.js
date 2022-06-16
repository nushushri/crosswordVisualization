let table;
let monthColor = "blue";
let rowNum = 185;
let rate = 7;

function preload()
{
  table = loadTable('crosswordTimes.csv', 'csv', 'header');
}
function setup() {
  createCanvas(1000,800);
  background('black');
  frameRate(rate);
}

function draw() {
    fill("black");
    stroke("black");
    rect(0, 0, 150, 50);
    if(rowNum > -1)
    {
      monthColorFun(table.getString(rowNum,0));
      stroke(monthColor);
      strokeWeight(1);
      noFill();
      textSize(16);
      text(table.getString(rowNum,1), 30, 30);
      ellipse(300, 300, int(table.getString(rowNum,2)),int(table.getString(rowNum, 3)));
      // ellipse(750, 300, int(table.getString(rowNum,4)),int(table.getString(rowNum, 5)));
      rowNum = rowNum - 1;
    }
  
}

function monthColorFun(month){
  if(month == "May")
    {
      monthColor = color(0, 255, 0);
    }
  if(month == "June")
    {
      monthColor=color(0, 89, 255);
    }
  if(month == "July")
    {
      monthColor = color(0, 255, 251);
    }
  if(month == "Aug")
    {
      monthColor = color(0, 255, 183);
    }
  if(month == "Sept")
    {
      monthColor = color(0, 255, 128);
    }
  if(month == "Oct")
    {
      monthColor = color(0, 255, 55);
    }
  if(month == "Nov")
    {
      monthColor = color(47, 255, 0);
    }
  if(month == "Dec")
    {
      monthColor = color(136, 255, 0);
    }
  if(month == "Jan")
    {
      monthColor = color(234, 255, 0);
    }
}