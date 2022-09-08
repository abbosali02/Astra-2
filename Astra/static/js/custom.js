document.addEventListener("DOMContentLoaded", function(event){
  
//  get a reference to the animation-wrapper
  const animWrapper = document.querySelector(".animation-wrapper");
  const loadWrapper = document.querySelector(".run-once");
  
//  get the 'animationSeen' cookie and store in a variable
  const seenAnimation = Cookies.get('animationSeen');
  
//  if the 'animationSeen' cookie is undefined
  if(!seenAnimation){
//   display the loading-wrapper
    loadWrapper.style.display = "block";
    
//    show the page-wrapper
//    set the 'animationSeen' cookie to expire in 24h
    Cookies.set('animationSeen', 1, { expires:1 });
  } else {
//    else if the 'animationSeen' cookie exists
//    the user has already seen the animation
//    hide the loading-wrapper
    loadWrapper.style.visibility = "hidden";
//    show the page-wrapper
    animWrapper.style.display = "flex";
  }
  
});


















































































































