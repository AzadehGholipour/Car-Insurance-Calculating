function updateCarSeriesDropdown() {
  var carName = document.getElementById("carName");
  var carSeries = document.getElementById("carSeries");

  // Clear existing options
  carSeries.innerHTML = "<option value=''>--Select--</option>";

  var selectedValue = carName.value;

  var options = [];

  if (selectedValue === "bmw") {
      options = ["Z4", "iX", "X4"];
  } else if (selectedValue === "peugeot") {
      options = ["108", "208", "308", "408", "Rifter"];
  } else if (selectedValue === "ford") {
      options = ["Kuga", "Mustang", "Transit", "S-Max", "Focus"];
  } else if (selectedValue === "honda") {
      options = ["Ny1", "Odyssey", "ZR-V", "Ridgeline"];
  }

  // Add new options to the second dropdown
  options.forEach(function(option) {
      var opt = document.createElement("option");
      opt.value = option.toLowerCase();
      opt.textContent = option;
      carSeries.appendChild(opt);
  });
};


function calculatePremium() {
  const fire_ratio = 0.02;
  const theft_ratio = 0.15;
  const natural_disaster_ratio = 0.05;

  let premium = 0;
  let base_premium = 0;
  let coverage = 0;
  let discount = 0;
  let cost = parseFloat(document.getElementById('cost').value);
  
  let fire = document.getElementById('fire');
  let theft = document.getElementById('theft');
  let natural_disaster = document.getElementById('natural_disaster');
  
  let noclaim = document.getElementById('noclaim').value;
  
  if (!cost || isNaN(cost)) {
    alert("Please enter the cost of your car");
  } else {

    base_premium = cost * 0.014;

    if (fire.checked) {
      coverage += (fire_ratio * base_premium);
    };
    if (theft.checked) {
      coverage += (theft_ratio * base_premium);
    };
    if (natural_disaster.checked) {
      coverage += (natural_disaster_ratio * base_premium);
    };

    if (noclaim) {
      switch (noclaim) {
        case 'one_y':
          discount = base_premium * 0.15;
          break;
        case 'two_y':
          discount = base_premium * 0.3;
          break;
        case 'three_y':
          discount = base_premium * 0.45;
          break;
        case 'four_y':
          discount = base_premium * 0.6;
          break;
      };
    };
    premium = base_premium + coverage - discount;
    if (premium>=0) {
      document.getElementById("premium").innerText = premium.toFixed(2);
    } else {
      alert('ERROR!')
    };
  };
};


function load_form() {
  fetch('/check-auth-status/')
    .then(response => {
      if (response.status === 401) {
        alert('Please log in to your account, or register at first');
        return;
      };
      return response.json(); 
    })
    .then(data => {
      if (data && data.is_authenticated) {
        document.querySelector('#form-view').style.display = 'block';
        document.querySelector('#CarName').value = '';
        document.querySelector('#carSeries').value = '';
        document.querySelector('#license').value = '';
        document.querySelector('#VIN').value = '';
        document.querySelector('#year').value = '';
      };
    })
    .catch(error => {
      console.error('Error:', error);
    });
};
