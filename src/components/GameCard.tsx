import { Game } from "../hooks/useGames";
import { Card, HStack, Heading, Image, Text } from "@chakra-ui/react";
import PlatformIconList from "./PlatformIconList";
import CriticScore from "./CriticScore";
import getCroppedImageUrl from "../services/images_url";

interface props {
  game: Game;
}

const GameCard = ({ game }: props) => {
  return (
    <Card>
      <Image src={getCroppedImageUrl(game.background_image)} />
      <HStack justifyContent="space-between" padding={2}>
        <PlatformIconList
          platforms={game.parent_platforms.map((p) => p.platform)}
        />
        <CriticScore score={game.metacritic} />
      </HStack>
      <Heading fontSize="xl" padding={2}>
        {game.name}
      </Heading>
    </Card>
  );
};

export default GameCard;
