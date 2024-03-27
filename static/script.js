document.addEventListener("DOMContentLoaded", function() {
const r = document.querySelector(":root");
const bodyElement = document.body;
const randomizeElement = document.querySelector(".randomize");
const destinations = [
  
  {
    name: "Taj Mahal",
    location: "India",
    img:
      'https://cdn.pixabay.com/photo/2023/08/19/13/26/ai-generated-8200484_1280.jpg',
  },
  {
    name: "Kolkata",
    location: "India",
    img: 'https://cdn.pixabay.com/photo/2019/09/25/06/31/victoria-memorial-4502719_1280.jpg',
  },
  {
    name: "Kerala",
    location: "India",
    img:
      'https://cdn.pixabay.com/photo/2017/02/09/16/11/houseboat-2052738_1280.jpg',
  },
  {
    name: "Hyderabad",
    location: "India",
    img:
      'https://cdn.pixabay.com/photo/2022/01/09/09/35/charminar-6925631_1280.jpg',
  },
  {
    name: "Nepal",
    location: "India",
    img:
      'https://cdn.pixabay.com/photo/2015/05/30/12/47/nepal-790336_1280.jpg',
  },
  {
    name: "Goa",
    location: "India",
    img:
      'https://cdn.pixabay.com/photo/2017/05/30/05/46/goa-2355883_1280.jpg',
  },
  {
    name: "Karnataka",
    location: "India",
    img:
      'https://cdn.pixabay.com/photo/2014/02/27/19/23/hanging-bridge-276142_1280.jpg',
  },
  {
    name: "Kashmir",
    location: "India",
    img:
      'https://cdn.pixabay.com/photo/2021/02/01/06/17/mountains-5969476_1280.jpg',
  },
  {
    name: "Punjab",
    location: "India",
    img:
      'https://cdn.pixabay.com/photo/2021/01/06/16/58/harmandir-sahib-5895031_1280.jpg',
  },
  {
    name: "Rajasthan",
    location: "India",
    img: 'https://cdn.pixabay.com/photo/2018/09/11/17/20/jaipur-3670085_1280.jpg',
  },
  {
    name: "Tamil Nadu",
    location: "India",
    img: 'https://cdn.pixabay.com/photo/2019/09/03/03/03/coonoor-4448487_1280.jpg',
  },
  {
    name: "Delhi",
    location: "India",
    img:
    'https://cdn.pixabay.com/photo/2013/03/14/05/55/temple-93446_1280.jpg',
  }
];
let nextDestination = destinations[1];

const getRandomDestination = () => {
  const randomId = Math.floor(Math.random() * destinations.length);
  return destinations[randomId];
};

const displayNextContent = () => {
  if (bodyElement.classList.contains("body--animated")) {
    return;
  }

  bodyElement.classList.add("body--animated");

  setTimeout(() => {
    r.style.setProperty("--img-current", `url(${nextDestination.img})`);
    r.style.setProperty("--text-current-title", `"${nextDestination.name}"`);
    r.style.setProperty("--text-current-subtitle", `"${nextDestination.location}"`);
    setTimeout(() => {
      bodyElement.classList.remove("body--animated");
      setTimeout(() => {
        nextDestination = getRandomDestination();
        r.style.setProperty("--img-next", `url(${nextDestination.img})`);
        r.style.setProperty("--text-next-title", `"${nextDestination.name}"`);
        r.style.setProperty("--text-next-subtitle", `"${nextDestination.location}"`);
      }, 1000);
    }, 1000);
  }, 1000);
};

randomizeElement.addEventListener("click", displayNextContent);

displayNextContent();
});
