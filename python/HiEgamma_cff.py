import FWCore.ParameterSet.Config as cms

# clustering sequence
from RecoEcal.EgammaClusterProducers.islandClusteringSequence_cff import *
from RecoEcal.EgammaClusterProducers.hybridClusteringSequence_cff import *
from RecoEcal.EgammaClusterProducers.multi5x5ClusteringSequence_cff import *
from RecoEcal.EgammaClusterProducers.multi5x5PreshowerClusteringSequence_cff import *
from RecoEcal.EgammaClusterProducers.preshowerClusteringSequence_cff import *
from RecoEcal.EgammaClusterProducers.dynamicHybridClusteringSequence_cff import *

hiEcalClusteringSequence = cms.Sequence(islandClusteringSequence*hybridClusteringSequence*dynamicHybridClusteringSequence*multi5x5ClusteringSequence*multi5x5PreshowerClusteringSequence*preshowerClusteringSequence)

# reco photon producer
from RecoEgamma.EgammaPhotonProducers.photonSequence_cff import *

photonCore.scHybridBarrelProducer = cms.InputTag("correctedIslandBarrelSuperClusters") # use island for the moment
photonCore.scIslandEndcapProducer = cms.InputTag("correctedIslandEndcapSuperClusters") # use island for the moment
photonCore.minSCEt = cms.double(8.0)
photons.minSCEtBarrel = cms.double(5.0)
photons.minSCEtEndcap = cms.double(15.0)
photons.minR9Barrel = cms.double(0.01)  #0.94
photons.minR9Endcap = cms.double(0.8)   #0.95
photons.maxHoverEEndcap = cms.double(0.5)  #0.5
photons.maxHoverEBarrel = cms.double(0.99)  #0.5
photons.primaryVertexProducer = cms.string('hiSelectedVertex') # replace the primary vertex
photons.isolationSumsCalculatorSet.trackProducer = cms.InputTag("hiSelectedTracks")


hiPhotonSequence = cms.Sequence(photonSequence)

# HI Egamma Isolation
from RecoHI.HiEgammaAlgos.HiEgammaIsolation_cff import *

# HI Ecal reconstruction
hiEcalClusters = cms.Sequence(hiEcalClusteringSequence)
hiEgammaSequence = cms.Sequence(hiPhotonSequence)
hiEcalClustersIsolation = cms.Sequence(hiEgammaSequence * hiEgammaIsolationSequence)

