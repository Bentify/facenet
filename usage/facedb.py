import os
from functools import reduce
import cv2
import ngtpy
import facenet.src.facenet as facenet
import uuid

class FaceDB:
    '''
    FaceDB     
    '''
    def __init__(self, face_embd_dim, facedb_folder, idx_folder=b'tmp', images_per_face=20, max_distance = 0.23):
        self.face_embd_dim = face_embd_dim
        self.facedb_folder = facedb_folder
        ngtpy.create(idx_folder, face_embd_dim, distance_type="Cosine")
        self.index = ngtpy.Index(idx_folder)
        self.images_per_face = images_per_face
        self.max_distance = max_distance
        self.face2identityId = {}
        self.dataset = []
        
    def initialize_db(self):
        '''
        TODO: load folders as ids, init index with existing face embeddings
        later: load centroid embedding from face.embeddding file to index
        '''
        if not os.path.exists(self.facedb_folder):
            os.makedirs(self.facedb_folder)
            return
        self.dataset = facenet.get_dataset(self.facedb_folder)
        if len(self.dataset) == 0:
            return
        #TODO: load folders as identityId then
        # for all faces added to index set face2identityId[indexId] = identityId      

    
    def _save_face_image(self, face, faceId, identityId):
        #cv2.imwrite("facedb-" + str(hash(face.embedding)) + ".png", face.image)
        fldr = self.facedb_folder+'/'+identityId
        if not os.path.exists(fldr):
            os.makedirs(fldr)
        cv2.imwrite(fldr+'/'+str(hash(face.embedding.tostring())) + ".png", face.image)
    
    def upsert_face(self, face):
        '''
        face = {embedding, image}
        '''
        #print(self.face2identityId)
        found = self.index.search(face.embedding, self.images_per_face)
        #print("found", found)
        #found_similar = reduce(self._filter,found, [])
        found_similar = list(filter(lambda x: x[1] < self.max_distance, found))
        if len(found_similar)>0 :
            nearest = found_similar[0]
            faceId, _ = nearest
            identityId = self.face2identityId[faceId]
            print('Found person:', identityId, 'distance:', _) 
        else:
            identityId = str(uuid.uuid1()) # new identity found 
            print('New person:', identityId)  

        if len(found_similar) < self.images_per_face:
            faceId = self.index.insert(face.embedding) - 1
            print('inserting id', faceId, identityId)
            self._save_face_image(face, faceId, identityId)
            self.index.build_index()
            self.face2identityId[faceId] = identityId 
        
        return identityId, faceId