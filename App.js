// 🔧 استبدل هذه الإعدادات بإعدادات مشروعك من Firebase
const firebaseConfig = {
  apiKey: "AIzaSyBcXbAI4TJ4LLDwtUxw51Oj-XI1LI0kCbY",
  authDomain: "caraboubou-19121.firebaseapp.com",
  projectId: "caraboubou-19121",
  storageBucket: "caraboubou-19121.appspot.com",
  messagingSenderId: "272615732857",
  appId: "1:272615732857:web:7daa2bfd3281cb6e5546a8",
};

firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();

const email = document.getElementById("email");
const password = document.getElementById("password");
const messageInput = document.getElementById("message");
const messagesDiv = document.getElementById("messages");

function signup() {
  auth.createUserWithEmailAndPassword(email.value, password.value)
    .then(() => alert("تم إنشاء الحساب"))
    .catch((err) => alert(err.message));
}

function login() {
  auth.signInWithEmailAndPassword(email.value, password.value)
    .then(() => {
      document.querySelector(".container").style.display = "none";
      document.querySelector(".chat-box").style.display = "block";
      listenMessages();
    })
    .catch((err) => alert(err.message));
}

function logout() {
  auth.signOut().then(() => {
    document.querySelector(".container").style.display = "block";
    document.querySelector(".chat-box").style.display = "none";
  });
}

function sendMessage() {
  const msg = messageInput.value;
  const user = auth.currentUser;
  if (msg && user) {
    db.ref("messages").push({
      text: msg,
      user: user.email,
      time: new Date().toLocaleTimeString()
    });
    messageInput.value = "";
  }
}

function listenMessages() {
  db.ref("messages").on("value", (snapshot) => {
    messagesDiv.innerHTML = "";
    snapshot.forEach((child) => {
      const msg = child.val();
      const el = document.createElement("div");
      el.textContent = `[${msg.time}] ${msg.user}: ${msg.text}`;
      messagesDiv.appendChild(el);
    });
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  });
}
