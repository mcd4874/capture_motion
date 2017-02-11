import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name="dwsxmzrpt",
    api_key="387981548284158",
    api_secret="o-lfpbw-L0mnBnC4B_iVBeV5tzU"
)

result = cloudinary.uploader.upload()


