document.addEventListener("DOMContentLoaded", () => {
    // Example for blocking/unblocking usage
    const blockUsage = document.getElementById("blockUsage");
    const unblockUsage = document.getElementById("unblockUsage");

    if (blockUsage) {
        blockUsage.addEventListener("click", () => {
            alert("Device usage blocked!");
        });
    }

    if (unblockUsage) {
        unblockUsage.addEventListener("click", () => {
            alert("Device usage unblocked!");
        });
    }
});