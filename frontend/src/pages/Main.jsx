import { useEffect, useState } from "../lib/dom";
import { createElement } from "../lib/createElement";

const MainPage = () => {
  const MoveTo2FA = () => {
    // gotoPage("http://10.31.5.2:8000/api/auth/login");
    window.location.href = "https://10.31.5.2/api/auth/login";
  };
  return (
    <div class="main-page">
      <h1 class="title">TRAnscendence</h1>
      <button type="button" class="large-btn" onclick={MoveTo2FA}>
        42 login
      </button>
    </div>
  );
};

export default MainPage;
