import multer from "multer";

// multer is to get the images and save them on the backend
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, "images/");
  },
  filename: (req, file, cb) => {
    const newName = file.mimetype.replace("/", ".");
    cb(null, newName);
  },
});

const upload = multer({ storage: storage });
export default upload;
