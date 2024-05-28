import os
from PIL import Image
import torch
from torch.utils.data import Dataset

class CustomDataset(Dataset):
    def __init__(self,root_dir, transform=None):
        self.root_dir =root_dir
        self.transform=transform
        self.x_list =self.load_data()

    def load_data(self):

        x_list = []

        for subject_dir in os.listdir(self.root_dir):
            sub_pth = os.path.join(self.root_dir, subject_dir)

            if os.path.isdir(sub_pth):

                for seq_dir in os.listdir(sub_pth):
                    seq_pth = os.path.join(sub_pth,seq_dir)

                    if os.path.isdir(seq_pth):
                        for frames in os.listdir(seq_pth):

                            if frames.endswith('.png'):
                                f_pth = os.path.join(seq_pth,frames)
                                x_list.append((f_pth,int(subject_dir)))
        return x_list

    def __len__(self):
        return len(self.x_list)

    def __getitem__(self,idx):

        img_pth,cls_label = self.x_list[idx]

        image = Image.open(img_pth).convert('RGB')

        if self.transform:
            image = self.transform(image)
        return image,cls_label

# execution
# from torchvision import transforms
# from torch.utils.data import DataLoader

# transform = transforms.Compose([transforms.Resize((224, 224)),
#     transforms.ToTensor(),transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])])

# dataset = CustomDataset(root_dir='', transform=transform)
# data_loader = DataLoader(dataset, batch_size=32, shuffle=True)
