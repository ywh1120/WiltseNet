/*
  * document.js 1.0
  *
  * Copyright 2011, hanausi (http://www.hanausi.com)
  * 
  * Depends:
  *    hanausi.js
  */
 var _document = {};

 /*
  * 한글과컴퓨터 hwp
  */
 _document.hwp = {};
 _document.hwp.minVersion = 0x05050117;
 _document.hwp.pHwpCtrl = null;
 _document.hwp.basePath = "http://hwp.saver.com:8022";
 /*
  * open hwp
  */
 _document.hwp.onStart = function(hwp){
     _document.hwp.pHwpCtrl = $("HwpCtrl");
     
     /*
      * version체크 한글이 설치되어있는지 유무를 판별한다.
      */
     if(!_document.hwp.version()){
         return;
     }
     
     /*
      * debug 모드
     */
     _document.hwp.pHwpCtrl.SetClientName("DEBUG");
  
     if(!_document.hwp.pHwpCtrl.Open(_document.hwp.basePath + hwp))
     {
         alert("파일(" + _document.hwp.basePath + hwp + ") 를 여는데 실패하였습니다.");
     }
  
     _document.hwp.pHwpCtrl.SetToolBar(-1, "TOOLBAR_MENU");
     _document.hwp.pHwpCtrl.SetToolBar(-1, "TOOLBAR_STANDARD");
     _document.hwp.pHwpCtrl.SetToolBar(-1, "TOOLBAR_FORMAT");
     _document.hwp.pHwpCtrl.SetToolBar(-1, "TOOLBAR_DRAW");
     _document.hwp.pHwpCtrl.SetToolBar(-1, "-TOOLBAR_TABLE");
     _document.hwp.pHwpCtrl.SetToolBar(-1, "-TOOLBAR_IMAGE");
     _document.hwp.pHwpCtrl.SetToolBar(-1, "-TOOLBAR_HEADERFOOTER");
     _document.hwp.pHwpCtrl.SetToolBar(0, "FilePreview, Print, Separator, Undo, Redo, Separator, Cut, Copy, Paste,"
     +"Separator, ParaNumberBullet, MultiColumn, SpellingCheck, HwpDic, Separator, PictureInsertDialog, MacroPlay1");
     _document.hwp.pHwpCtrl.SetToolBar(0, "Print, Separator, Undo, Redo, Separator, Cut, Copy, Paste,"
     +"Separator, ParaNumberBullet, MultiColumn, SpellingCheck, HwpDic, Separator, PictureInsertDialog, MacroPlay1");
     _document.hwp.pHwpCtrl.ShowToolBar(true);
     _document.hwp.pHwpCtrl.ShowStatusBar(1);
 };
 _document.hwp.getBasePath = function(){
     //BasePath를 구한다.
     var loc = unescape(document.location.href);
     var lowercase = loc.toLowerCase(loc);
     if (lowercase.indexOf("http://") == 0) // Internet
     {
         return loc.substr(0,loc.lastIndexOf("/") + 1);//BasePath 생성
    }

     /*
      * local
      */
     var path = loc.replace(/.{2,}:\/{2,}/, ""); // file:/// 를 지워버린다.
     return path.substr(0,path.lastIndexOf("/") + 1);//BasePath 생성
};
 _document.hwp.version = function(){
     /*
      * 설치확인
     */
     if(_document.hwp.pHwpCtrl.getAttribute("Version") == null)
     {
         alert("한글(HwpCrtl)이 설치되지 않았습니다.");
         return false;
     }
     
     /*
      * 버젼 확인
     */
     var currentVersion = _document.hwp.pHwpCtrl.Version;
     if(currentVersion < _document.hwp.minVersion)
     {
         alert("한글(HwpCrtl)의 버젼이 낮아서 정상적으로 동작하지 않을 수 있습니다.\n"+
             "최신 버젼으로 업데이트하기를 권장합니다.\n\n"+
             "현재 버젼: 0x" + currentVersion.toString(16) + "\n"+
             "권장 버젼: 0x" + _document.hwp.minVersion.toString(16) + " 이상"            
             );
     }
     
     return true;
 };
