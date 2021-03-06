''' The `Extractor` hierarchy contains Transformer classes that take a `Stim`
of any type as input and return extracted feature information (rather than
another `Stim` instance).
'''

from .base import Extractor, ExtractorResult, merge_results
from .api import (IndicoAPITextExtractor,
                  IndicoAPIImageExtractor,
                  ClarifaiAPIImageExtractor,
                  ClarifaiAPIVideoExtractor,
                  GoogleVisionAPIFaceExtractor,
                  GoogleVisionAPILabelExtractor,
                  GoogleVisionAPIPropertyExtractor,
                  GoogleVisionAPISafeSearchExtractor,
                  GoogleVisionAPIWebEntitiesExtractor,
                  GoogleVideoIntelligenceAPIExtractor,
                  GoogleVideoAPILabelDetectionExtractor,
                  GoogleVideoAPIShotDetectionExtractor,
                  GoogleVideoAPIExplicitDetectionExtractor,
                  GoogleLanguageAPIExtractor,
                  GoogleLanguageAPIEntityExtractor,
                  GoogleLanguageAPISentimentExtractor,
                  GoogleLanguageAPISyntaxExtractor,
                  GoogleLanguageAPITextCategoryExtractor,
                  GoogleLanguageAPIEntitySentimentExtractor,
                  MicrosoftAPIFaceExtractor,
                  MicrosoftAPIFaceEmotionExtractor,
                  MicrosoftVisionAPIExtractor,
                  MicrosoftVisionAPITagExtractor,
                  MicrosoftVisionAPICategoryExtractor,
                  MicrosoftVisionAPIImageTypeExtractor,
                  MicrosoftVisionAPIColorExtractor,
                  MicrosoftVisionAPIAdultExtractor)
from .audio import (LibrosaFeatureExtractor,
                    STFTAudioExtractor,
                    MeanAmplitudeExtractor,
                    SpectralCentroidExtractor,
                    SpectralBandwidthExtractor,
                    SpectralContrastExtractor,
                    SpectralRolloffExtractor,
                    PolyFeaturesExtractor,
                    RMSEExtractor,
                    ZeroCrossingRateExtractor,
                    ChromaSTFTExtractor,
                    ChromaCQTExtractor,
                    ChromaCENSExtractor,
                    MelspectrogramExtractor,
                    MFCCExtractor,
                    TonnetzExtractor,
                    TempogramExtractor,
                    RMSExtractor,
                    SpectralFlatnessExtractor,
                    OnsetDetectExtractor,
                    OnsetStrengthMultiExtractor,
                    TempoExtractor,
                    BeatTrackExtractor,
                    HarmonicExtractor,
                    PercussiveExtractor)
from .image import (BrightnessExtractor, SaliencyExtractor, SharpnessExtractor,
                    VibranceExtractor, FaceRecognitionFaceEncodingsExtractor,
                    FaceRecognitionFaceLandmarksExtractor,
                    FaceRecognitionFaceLocationsExtractor)
from .models import TensorFlowInceptionV3Extractor
from .text import (ComplexTextExtractor, DictionaryExtractor,
                   PredefinedDictionaryExtractor, LengthExtractor,
                   NumUniqueWordsExtractor, PartOfSpeechExtractor,
                   WordEmbeddingExtractor, TextVectorizerExtractor,
                   VADERSentimentExtractor, SpaCyExtractor)
from .video import (FarnebackOpticalFlowExtractor)

__all__ = [
    'Extractor',
    'ExtractorResult',
    'IndicoAPITextExtractor',
    'IndicoAPIImageExtractor',
    'ClarifaiAPIImageExtractor',
    'ClarifaiAPIVideoExtractor',
    'STFTAudioExtractor',
    'MeanAmplitudeExtractor',
    'LibrosaFeatureExtractor',
    'SpectralCentroidExtractor',
    'SpectralBandwidthExtractor',
    'SpectralContrastExtractor',
    'SpectralRolloffExtractor',
    'PolyFeaturesExtractor',
    'RMSEExtractor',
    'ZeroCrossingRateExtractor',
    'ChromaSTFTExtractor',
    'ChromaCQTExtractor',
    'ChromaCENSExtractor',
    'MelspectrogramExtractor',
    'MFCCExtractor',
    'TonnetzExtractor',
    'TempogramExtractor',
    'GoogleVisionAPIFaceExtractor',
    'GoogleVisionAPILabelExtractor',
    'GoogleVisionAPIPropertyExtractor',
    'GoogleVisionAPISafeSearchExtractor',
    'GoogleVisionAPIWebEntitiesExtractor',
    'GoogleVideoIntelligenceAPIExtractor',
    'GoogleVideoAPILabelDetectionExtractor',
    'GoogleVideoAPIShotDetectionExtractor',
    'GoogleVideoAPIExplicitDetectionExtractor',
    'GoogleLanguageAPIExtractor',
    'GoogleLanguageAPIEntityExtractor',
    'GoogleLanguageAPISentimentExtractor',
    'GoogleLanguageAPISyntaxExtractor',
    'GoogleLanguageAPITextCategoryExtractor',
    'GoogleLanguageAPIEntitySentimentExtractor',
    'BrightnessExtractor',
    'SaliencyExtractor',
    'SharpnessExtractor',
    'VibranceExtractor',
    'FaceRecognitionFaceEncodingsExtractor',
    'FaceRecognitionFaceLandmarksExtractor',
    'FaceRecognitionFaceLocationsExtractor',
    'MicrosoftAPIFaceExtractor',
    'MicrosoftAPIFaceEmotionExtractor',
    'MicrosoftVisionAPIExtractor',
    'MicrosoftVisionAPITagExtractor',
    'MicrosoftVisionAPICategoryExtractor',
    'MicrosoftVisionAPIImageTypeExtractor',
    'MicrosoftVisionAPIColorExtractor',
    'MicrosoftVisionAPIAdultExtractor',
    'TensorFlowInceptionV3Extractor',
    'ComplexTextExtractor',
    'DictionaryExtractor',
    'PredefinedDictionaryExtractor',
    'LengthExtractor',
    'NumUniqueWordsExtractor',
    'PartOfSpeechExtractor',
    'FarnebackOpticalFlowExtractor',
    'WordEmbeddingExtractor',
    'TextVectorizerExtractor',
    'VADERSentimentExtractor',
    'merge_results', 
    'SpaCyExtractor',
    'RMSExtractor',
    'SpectralFlatnessExtractor'
    'OnsetDetectExtractor',
    'OnsetStrengthMultiExtractor',
    'TempoExtractor',
    'BeatTrackExtractor',
    'HarmonicExtractor',
    'PercussiveExtractor'
]
