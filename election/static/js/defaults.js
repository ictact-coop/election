
/**
 * 이메일 형식 체크
 *
 * @param 데이터
 */
function emailCheck(email) {
  var exptext = /^[A-Za-z0-9_\.\-]+@[A-Za-z0-9\-]+\.[A-Za-z0-9\-]+/;
  if(exptext.test(email) == false) {
    // 이메일 형식이 알파벳+숫자@알파벳+숫자.알파벳+숫자 형식이 아닐경우
    alert("이메일형식이 올바르지 않습니다.");
    return false;
  }
  return true;
}

/**
 * 특수문자 여부 체크
 *
 * @param 데이터
 */
function checkSpecial(str) {
  var special_pattern = /[`~!@#$%^&*|\\\'\";:\/?]/gi;
  if (special_pattern.test(str) == true) {
    return 0;
  } else {
    return -1;
  }
}

/**
 * 전화번호 포맷으로 변환
 *
 * @param 데이터
 */
function formatPhone(phoneNum) {
  if(isPhone(phoneNum)) {
    var rtnNum;
    var regExp =/(02)([0-9]{3,4})([0-9]{4})$/;
    var myArray;
    if(regExp.test(phoneNum)){
      myArray = regExp.exec(phoneNum);
      rtnNum = myArray[1]+'-' + myArray[2]+'-'+myArray[3];
      return rtnNum;
    } else {
      regExp =/(0[3-9]{1}[0-9]{1})([0-9]{3,4})([0-9]{4})$/;
      if(regExp.test(phoneNum)){
        myArray = regExp.exec(phoneNum);
        rtnNum = myArray[1]+'-'+myArray[2]+'-'+myArray[3];
        return rtnNum;
      } else {
        return phoneNum;
      }
    }
  } else {
    return phoneNum;
  }
}

/**
 * 핸드폰번호 포맷으로 변환
 *
 * @param 데이터
 */
function formatMobile(phoneNum) {
  if(isMobile(phoneNum)) {
    var rtnNum;
    var regExp =/(01[016789])([1-9]{1}[0-9]{2,3})([0-9]{4})$/;
    var myArray;
    if(regExp.test(phoneNum)){
      myArray = regExp.exec(phoneNum);
      rtnNum = myArray[1]+'-'+myArray[2]+'-'+myArray[3];
      return rtnNum;
    } else {
      return phoneNum;
    }
  } else {
    return phoneNum;
  }
}

/**
 * 전화번호 형식 체크
 *
 * @param 데이터
 */
function isPhone(phoneNum) {
  var regExp =/(02)([0-9]{3,4})([0-9]{4})$/;
  var myArray;
  if(regExp.test(phoneNum)){
    myArray = regExp.exec(phoneNum);
    return true;
  } else {
    regExp =/(0[3-9]{1}[0-9]{1})([0-9]{3,4})([0-9]{4})$/;
    if(regExp.test(phoneNum)){
      myArray = regExp.exec(phoneNum);
      return true;
    } else {
      return false;
    }
  }
}

/**
 * 핸드폰번호 형식 체크
 *
 * @param 데이터
 */
function isMobile(phoneNum) {
  var regExp =/(01[016789])([1-9]{1}[0-9]{2,3})([0-9]{4})$/;
  var myArray;
  if(regExp.test(phoneNum)){
    myArray = regExp.exec(phoneNum);
    return true;
  } else {
    return false;
  }
}

/* 출처: https://holybell87.tistory.com/22#.YD265NzlKUk [K's 개발이야기] */
