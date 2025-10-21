
const age = prompt("Your age:");

const membershipInput = prompt("Do you have Membership (Yes/no):").toLowerCase();
const hasMembership = membershipInput === "yes" || membershipInput === "ja";


if (age >= 18 && hasMembership) {
    alert("OK. Access granted.");
} else {
    let reason = "Access denied. Reason: ";
    if (age < 18 && !hasMembership) {
    reason += "you are under 18 and do not have an active membership.";
    } else if (age < 18) {
    reason += "you are under 18.";
    } else if (!hasMembership) {
    reason += "you do not have an active membership.";
    }
    alert(reason);
}



const tempInput = prompt("Enter the current room temperature (°C):");
const temperature = parseInt(tempInput, 10);


if (temperature < 18) {
    alert("Too cold.");
} else if (temperature >= 18 && temperature <= 22) {
    alert("Pleasant.");
} else {
    alert("Too warm.");
}
