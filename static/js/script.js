 document.addEventListener("DOMContentLoaded", () => {

    const fileInput = document.querySelector('input[type="file"]');
    const form = document.querySelector("form");

    // Create preview container
    const previewContainer = document.createElement("div");
    previewContainer.className = "preview-container";

    const previewImage = document.createElement("img");
    previewImage.className = "preview-image";
    previewImage.style.display = "none";

    const fileText = document.createElement("p");
    fileText.className = "file-name";

    previewContainer.appendChild(previewImage);
    previewContainer.appendChild(fileText);

    const uploadBox = document.querySelector(".upload-box");
    uploadBox.appendChild(previewContainer);

    // File selection
    fileInput.addEventListener("change", function () {

        const file = this.files[0];

        if (!file) return;

        // Check image type
        const allowedTypes = [
            "image/jpeg",
            "image/jpg",
            "image/png",
            "image/webp"
        ];

        if (!allowedTypes.includes(file.type)) {
            alert("Please select JPG, JPEG, PNG or WEBP image.");
            this.value = "";
            return;
        }

        // Show filename
        fileText.innerHTML = `<strong>Selected:</strong> ${file.name}`;

        // Image Preview
        const reader = new FileReader();

        reader.onload = function (e) {
            previewImage.src = e.target.result;
            previewImage.style.display = "block";
        };

        reader.readAsDataURL(file);
    });

    // Loading state when searching
    form.addEventListener("submit", function () {

        const button = document.querySelector("button");

        button.disabled = true;
        button.innerHTML = "⏳ Searching Similar Products...";

    });

});